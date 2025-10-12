export enum UserRole {
  ADMIN = "admin",
  COUNSELLOR = "counsellor",
  BORROWER = "borrower",
}

/*NOTE
In this we are using console.log() but in reality we can have another db for our log saving
*/

export function logAccessAttempt(
  userId: string,
  role: UserRole,
  endpoint: string,
  status: "SUCCESS" | "FAILURE",
  reason?: string
): void {
  const logEntry = {
    timestamp: new Date().toISOString(),
    control: "CC6.1 - Logical Access Control",
    event_type: "API_ACCESS",
    user_id: userId,
    user_role: role,
    endpoint: endpoint,
    status: status,
    reason: reason || "N/A",
  };
  // In a real system, this sends the log to a secure, loggin service/db which is immutable so that no one can edit that
  console.log("ACCESS ARTIFACT GENERATED:", JSON.stringify(logEntry));
}

//this is the log for deletion of data ( when we delete user data after our access will proove that we donot store user data )
export function logDataDeletion(userId: string, dataIdentifier: string): void {
  const logEntry = {
    timestamp: new Date().toISOString(),
    control: "A.8.10 - Information Deletion", // ISO 27001 Reference: Proves policy adherence.
    event_type: "DATA_DELETION",
    data_id: dataIdentifier,
    status: "COMPLETE",
    compliance_policy: "P-DR-001 (7-year FinTech Retention)", // Mock Policy ID
    data_owner: userId,
  };
  console.log("🗑️ DELETION ARTIFACT GENERATED:", JSON.stringify(logEntry));
}
