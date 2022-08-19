from sqlalchemy import Column, Integer, String


from .database import Base

class Agent(Base):
    __tablename__ = "agents"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(40))
    email = Column(String(40))
    firstname = Column(String(40))
    lastname = Column(String(40))
    password_hash = Column(String(240))