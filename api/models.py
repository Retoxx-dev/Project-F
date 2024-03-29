from sqlalchemy import Column, ForeignKey, Integer, String, DateTime

from datetime import datetime

from .database import Base

class Ticket(Base):
    __tablename__ = "tickets"
    id = Column(Integer, primary_key=True, index=True)
    summary = Column(String(240))
    description = Column(String(240))
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=True)
    status_id = Column(Integer, ForeignKey('statuses.id'), nullable=True)
    level_id = Column(Integer, ForeignKey('levels.id'), nullable=True)
    agent_id = Column(Integer, ForeignKey('agents.id'), nullable=True)
    ticket_type_id = Column(Integer, ForeignKey('tickettypes.id'), nullable=True)
    date_occured = Column(DateTime, default=datetime.utcnow)
    
    
    
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
    
class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(40))
    email = Column(String(40))
    firstname = Column(String(40))
    lastname = Column(String(40))
    
class Agent(Base):
    __tablename__ = "agents"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(40))
    email = Column(String(40))
    firstname = Column(String(40))
    lastname = Column(String(40))
    password_hash = Column(String(240))