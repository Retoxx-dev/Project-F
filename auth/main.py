from fastapi import Depends, FastAPI, HTTPException

from sqlalchemy.orm import Session

from .database import SessionLocal

from . import schemas, crud, token_gen

app = FastAPI(
    swagger_ui_parameters={"defaultModelsExpandDepth": -1}
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#Auth
@app.post('/api/auth/', tags=["Authorize"])
def authorize(auth: schemas.Auth, db: Session = Depends(get_db)):
    user = crud.verify_email(db=db, email=auth.email)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    verify_password = crud.verify_password(db=db, password=auth.password, hashed_password=user.password_hash)
    if not verify_password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    access_token = token_gen.create_access_token(data={"sub": user.email})
    
    return {'access_token' : access_token}