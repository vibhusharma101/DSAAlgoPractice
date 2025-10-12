
import * as crypto from 'crypto';

const ENCRYPTION_KEY = 'a_very_secret_32_byte_key_for_aes256!'; // 32 bytes for AES-256
const IV_LENGTH = 16; // For AES-256-CBC


//for details like bank acc info etc we are using encryption ( so that we can decrypt the data later )
export function encryptSensitiveData(text: string): string {
    const iv = crypto.randomBytes(IV_LENGTH);
    const cipher = crypto.createCipheriv('aes-256-cbc', Buffer.from(ENCRYPTION_KEY), iv);
    
    let encrypted = cipher.update(text, 'utf8', 'hex');
    encrypted += cipher.final('hex');
    
    // Return the initialization vector (IV) and the encrypted data, joined by a colon.
    return iv.toString('hex') + ':' + encrypted;
}

export function decryptSensitiveData(text: string): string {
    const textParts = text.split(':');
    const iv = Buffer.from(textParts.shift()!, 'hex');
    const encryptedText = textParts.join(':');
    
    const decipher = crypto.createDecipheriv('aes-256-cbc', Buffer.from(ENCRYPTION_KEY), iv);
    
    let decrypted = decipher.update(encryptedText, 'hex', 'utf8');
    decrypted += decipher.final('utf8');
    
    return decrypted;
}



/**
 * for passwords etc where we donot need to access the data only check the correctness we are using 
 * hashing sha256 for security
 */
export function generateSensitiveDataHash(sensitiveData: string): string {
  const hash = crypto
    .createHash('sha256')
    .update(sensitiveData)
    .digest('hex');
    
  const logEntry = {
    timestamp: new Date().toISOString(),
    control: 'PI4.1 - Cryptographic Integrity Check',
    event_type: 'DATA_HASH_CREATION',
    data_fingerprint: hash,
  };
  
  console.log('🔗 HASH ARTIFACT GENERATED:', JSON.stringify(logEntry));
  
  return hash;
}

// we are using this to verify whether someone has changed our hash or not, just an additional check 
// for Processing Integrity (a key SOC 2 criterion), like it will help us to not send our corrupt data to any
// third party service as we will already check it.
export function verifySensitiveDataHash(sensitiveData: string, expectedHash: string): boolean {
    const calculatedHash = crypto
        .createHash('sha256')
        .update(sensitiveData)
        .digest('hex');
    return calculatedHash === expectedHash;
}