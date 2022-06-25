from sqlalchemy import Column, ForeignKey, Integer, String, DateTime

from sqlalchemy.orm import relationship

from datetime import datetime

from .database import Base

class Ticket(Base):
    __tablename__ = "tickets"
    id = Column(Integer, primary_key=True, index=True)
    summary = Column(String(240))
    description = Column(String(240))
    customer_id = Column(Integer, ForeignKey('customers.id'))
    status_id = Column(Integer, ForeignKey('statuses.id'))
    level_id = Column(Integer, ForeignKey('levels.id'))
    agent_id = Column(Integer, ForeignKey('agents.id'))
    ticket_type_id = Column(Integer, ForeignKey('tickettypes.id'))
    date_occured = Column(DateTime, default=datetime.utcnow)
    closure_note = Column(String(240), nullable=True)
    
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
    
class Agent(Base):
    __tablename__ = "agents"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(40))
    email = Column(String(40))
    firstname = Column(String(40))
    lastname = Column(String(40))
    password_hash = Column(String(240))
    
class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(40))
    email = Column(String(40))
    firstname = Column(String(40))
    lastname = Column(String(40))
    