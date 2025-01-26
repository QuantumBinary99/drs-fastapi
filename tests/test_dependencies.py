from fastapi import HTTPException
from app.dependencies import verify_basic_auth, verify_bearer_auth
from fastapi.security import HTTPBasicCredentials, HTTPAuthorizationCredentials

def test_verify_basic_auth_valid():
    # Simulate valid BasicAuth credentials
    credentials = HTTPBasicCredentials(username="admin", password="secret")
    assert verify_basic_auth(credentials) == "admin"

def test_verify_basic_auth_invalid():
    # Simulate invalid BasicAuth credentials
    credentials = HTTPBasicCredentials(username="admin", password="wrong")
    try:
        verify_basic_auth(credentials)
    except HTTPException as e:
        assert e.status_code == 401
        assert e.detail == "Invalid username or password"

def test_verify_bearer_auth_valid():
    # Simulate valid BearerAuth token
    credentials = HTTPAuthorizationCredentials(scheme="Bearer", credentials="fake-token")
    assert verify_bearer_auth(credentials) == "admin"

def test_verify_bearer_auth_invalid():
    # Simulate invalid BearerAuth token
    credentials = HTTPAuthorizationCredentials(scheme="Bearer", credentials="invalid-token")
    try:
        verify_bearer_auth(credentials)
    except HTTPException as e:
        assert e.status_code == 401
        assert e.detail == "Invalid or expired token"