// src/server.ts

import express, { Request, Response } from 'express';
import { authorizeRole } from './authMiddleware'; 
import { logDataDeletion, UserRole } from './complianceLogger';
import { decryptSensitiveData, encryptSensitiveData, generateSensitiveDataHash } from './cryptoUtils'; 

const app = express();
const PORT = 3300;

const MOCK_DB: { [key: string]: string } = {}; 


app.use(express.json());

// ENDPOINT 1: Secure Data Deletion ( Only Admins like our core team will be able to this)
// Compliance Goal: Data Retention Policy (ISO 27001 A.8.10)

app.delete(
  '/api/v1/data/secure-delete/:id',
  authorizeRole([UserRole.ADMIN]),
  (req: Request, res: Response) => {
    const dataId = req.params.id;
    
    logDataDeletion((req as any).user.id, dataId!!);
    res.status(200).send(`Data ID ${dataId} securely deleted and compliance artifact generated.`);

  }
);

// ENDPOINT 2: View Borrower Data ( only the councellors(debt collectors) will be able to see that )
// Compliance Goal: Least Privilege / Confidentiality (SOC 2 CC6.1)

app.get(
  '/api/v1/data/borrower/:id',
  authorizeRole([UserRole.ADMIN, UserRole.COUNSELLOR]),
  (req: Request, res: Response) => {
    
    //call service for fetching // 

    res.status(200).json({ 
      message: `Borrower data for ${req.params.id} fetched securely.`,
      retrieved_by: (req as any).user.id,
    });
  }
);

// ENDPOINT 3: Process Sensitive Information (Integrity Check)
// Compliance Goal: Processing Integrity (SOC 2 PI4.1) & Confidentiality

app.post(
  '/api/v1/data/process-pii',
  authorizeRole([UserRole.ADMIN, UserRole.COUNSELLOR]),
  (req: Request, res: Response) => {
    const { borrowerId, sensitiveInfo } = req.body;
    
    if (!borrowerId || !sensitiveInfo) {
      return res.status(400).send('Missing borrowerId or sensitiveInfo.');
    }

    // in this in case of passwords this will be used and in another case
    // our 2way encryption function etc will be used
    const dataHash = generateSensitiveDataHash(sensitiveInfo);

    // now we store the data after hashing etc.//
    
    res.status(200).json({
      message: `Sensitive data received, integrity hash created.`,
      borrower_id: borrowerId,
      integrity_artifact: dataHash, // Passed to the next system for verification
      status: 'Ready for secure downstream processing.',
    });
  }
);

// -------------------------------------------------------------------
// NEW ENDPOINT 4: Store Sensitive Data (Encryption applied upon storage)
// -------------------------------------------------------------------
app.post(
  '/api/v1/data/store-bank-details',
  authorizeRole([UserRole.ADMIN]), // High Privilege Required to store new data
  (req: Request, res: Response) => {
    const { borrowerId, bankDetails } = req.body;
    
    if (!borrowerId || !bankDetails) {
      return res.status(400).send('Missing ID or bank details.');
    }

    // 🎯 CRITICAL CONTROL: Encrypt data before storage (Data-at-Rest Confidentiality)
    const encryptedData = encryptSensitiveData(bankDetails);
    
    MOCK_DB[borrowerId] = encryptedData;
    
    res.status(200).json({
      message: `Bank details stored securely and encrypted.`,
      borrower_id: borrowerId,
      status: 'Encrypted data stored in mock DB.',
      // NEVER expose the encrypted data or key in the response!
    });
  }
);


// -------------------------------------------------------------------
// NEW ENDPOINT 5: Fetch & Decrypt Sensitive Data (Requires high-privilege access)
// -------------------------------------------------------------------
app.get(
  '/api/v1/data/fetch-bank-details/:id',
  // RBAC Control: Only Admin/Counsellor role can fetch and decrypt
  authorizeRole([UserRole.ADMIN, UserRole.COUNSELLOR]), 
  (req: Request, res: Response) => {
    const borrowerId = req.params.id!!;
    const encryptedData = MOCK_DB[borrowerId];
    
    if (!encryptedData) {
      return res.status(404).send('Borrower data not found or not yet stored.');
    }

    // 🎯 CRITICAL ACTION: Decrypt data in memory for immediate use
    // NOTE: This raw data must be destroyed from memory immediately after use.
    const decryptedData = decryptSensitiveData(encryptedData);

    res.status(200).json({
      message: `Bank details retrieved and decrypted in memory.`,
      borrower_id: borrowerId,
      // 🚨 CRITICAL: In a real app, this data would be masked or sent directly 
      // to the UI. We expose it here only to prove the decryption worked.
      decrypted_bank_details: decryptedData 
    });
  }
);



app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});