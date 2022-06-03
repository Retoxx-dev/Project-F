from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from datetime import datetime

from .database import Base

class Ticket(Base):
    __tablename__ = "tickets"
    id = Column(Integer, primary_key=True, index=True)
    summary = Column(String(60))
    description = Column(String(240))
    username = Column(String(40))
    status_id = Column(Integer, ForeignKey('statuses.id'))
    level_id = Column(Integer, ForeignKey('levels.id'))
    ticket_type_id = Column(Integer, ForeignKey('tickettypes.id'))
    date_occured = Column(DateTime, default=datetime.utcnow)
    closure_note = Column(String(200), nullable=True)
    
class Status(Base):
    __tablename__ = "statuses"
    id = Column(Integer, primary_key=True, index=True)
    status_name = Column(String(30), unique=True)
    
class Level(Base):
    __tablename__ = "levels"
    id = Column(Integer, primary_key=True, index=True)
    level_name = Column(String(30), unique=True)
    
class TicketType(Base):
    __tablename__ = "tickettypes"
    id = Column(Integer, primary_key=True, index=True)
    ticket_type_name = Column(String(30), unique=True)
    