from sqlalchemy.orm import Session

from . import models, schemas

#Tickets
def get_ticket(db: Session, ticket_id: int):
    return db.query(models.Ticket).filter(models.Ticket.id == ticket_id).first()

def get_all_tickets(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Ticket).offset(skip).limit(limit).all()

#Statuses
def get_all_statuses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Status).offset(skip).limit(limit).all()

def get_status(db: Session, status_id: int):
    return db.query(models.Status).filter(models.Status.id == status_id).first()

#Levels
def get_all_levels(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Level).offset(skip).limit(limit).all()

def get_level(db: Session, level_id: int):
    return db.query(models.Level).filter(models.Level.id == level_id).first()

#TicketTypes
def get_all_ticket_types(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.TicketType).offset(skip).limit(limit).all()

def get_ticket_type(db: Session, ticket_type_id: int):
    return db.query(models.TicketType).filter(models.TicketType.id == ticket_type_id).first()
