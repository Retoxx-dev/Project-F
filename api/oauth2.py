from fastapi.security import OAuth2PasswordBearer
from fastapi import HTTPException, Depends, status
from . import token_gen

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth")

def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    return token_gen.verify_token(token, credentials_exception)
    