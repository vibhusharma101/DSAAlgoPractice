import { Request, Response, NextFunction } from 'express';
import { logAccessAttempt, UserRole } from './complianceLogger';

// mock function, in prod these roles will be fetched by a service etc.
const mockUserLookup = (token: string) => {
  if (token.includes('ADMIN_TOKEN')) return { id: 'U1001', role: UserRole.ADMIN };
  if (token.includes('COUNSELLOR_TOKEN')) return { id: 'U2002', role: UserRole.COUNSELLOR };
  if (token.includes('BORROWER_TOKEN')) return { id: 'U3003', role: UserRole.BORROWER };
  return null;
};


export const authorizeRole = (allowedRoles: UserRole[]) => {
  return (req: Request, res: Response, next: NextFunction) => {
    const token = req.headers.authorization || '';
    const user = mockUserLookup(token);
    const endpoint = req.originalUrl;
    
    if (!user) {
      logAccessAttempt('GUEST', UserRole.BORROWER, endpoint, 'FAILURE', 'Missing or Invalid Credentials');
      return res.status(401).send('Access Denied: Missing credentials.');
    }

    const hasPermission = allowedRoles.includes(user.role);

    if (hasPermission) {
      (req as any).user = user; 
      logAccessAttempt(user.id, user.role, endpoint, 'SUCCESS');
      next();
    } else {
      const reason = `Role '${user.role}' not permitted on this endpoint.`;
      logAccessAttempt(user.id, user.role, endpoint, 'FAILURE', reason);
      return res.status(403).send(`Access Forbidden: Role not permitted.`);
    }
  };
};