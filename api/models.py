from sqlalchemy import Column, ForeignKey, Integer, String
#from sqlalchemy.orm import relationship

from .database import Base

class Ticket(Base):
    __tablename__ = "Tickets"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(20), unique=True, index=True)