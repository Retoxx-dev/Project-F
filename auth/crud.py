from sqlalchemy.orm import Session

from . import models

from passlib.hash import bcrypt

#Auth
def verify_email(db: Session, email: str):
    return db.query(models.Agent).filter(models.Agent.email == email).first()

def verify_password(db: Session, password: str, hashed_password: str):
    return bcrypt.verify(password, hashed_password)