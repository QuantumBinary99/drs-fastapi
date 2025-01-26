from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials, HTTPBearer, HTTPAuthorizationCredentials
from typing import Optional

# Security schemes
security_basic = HTTPBasic()
security_bearer = HTTPBearer()

# Mock user database (replace with real authentication logic)
fake_users_db = {
    "admin": {
        "username": "admin",
        "password": "secret",
        "scopes": ["drs:read", "drs:write"],
    }
}

# Mock token database (replace with real token validation logic)
fake_tokens_db = {
    "fake-token": {
        "username": "admin",
        "scopes": ["drs:read", "drs:write"],
    }
}

def verify_basic_auth(credentials: HTTPBasicCredentials = Depends(security_basic)):
    """
    Verify BasicAuth credentials.
    """
    user = fake_users_db.get(credentials.username)
    if user is None or user["password"] != credentials.password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username

def verify_bearer_auth(credentials: HTTPAuthorizationCredentials = Depends(security_bearer)):
    """
    Verify BearerAuth token.
    """
    token = credentials.credentials
    if token not in fake_tokens_db:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return fake_tokens_db[token]["username"]