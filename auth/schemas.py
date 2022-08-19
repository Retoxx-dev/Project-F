from pydantic import BaseModel


#Auth
class Auth(BaseModel):
    email: str
    password: str
    
    
#Token
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None