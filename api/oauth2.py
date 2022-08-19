from fastapi.security import OAuth2PasswordBearer
from fastapi import HTTPException, Depends, status
from . import ver_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth")

def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    return ver_token.verify_token(token, credentials_exception)
    