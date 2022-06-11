from sqlalchemy.orm import Session

from . import models, schemas

from fastapi.encoders import jsonable_encoder

#Tickets
def get_ticket(db: Session, ticket_id: int):
    return db.query(models.Ticket).filter(models.Ticket.id == ticket_id).first()

def get_all_tickets(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Ticket).offset(skip).limit(limit).all()

def post_ticket(db: Session, ticket: schemas.TicketCreate):
    ticket = models.Ticket(
        summary = ticket.summary,
        description = ticket.description,
        status_id = ticket.status_id,
        level_id = ticket.level_id,
        ticket_type_id = ticket.ticket_type_id,
        closure_note = ticket.closure_note,
        )
    db.add(ticket)
    db.commit()
    db.refresh(ticket)
    return ticket

def delete_ticket(db: Session, ticket_id: int):
    ticket_to_delete = db.query(models.Ticket).filter(models.Ticket.id == ticket_id).first()
    db.delete(ticket_to_delete)
    db.commit()
    return schemas.ResponseModel(details=f"Ticket {ticket_id} has been deleted")

def put_ticket(db: Session, db_obj, obj_in):
    obj_data = jsonable_encoder(db_obj)
    if isinstance(obj_in, dict):
        update_data = obj_in
    else:
        update_data = obj_in.dict(exclude_unset=True)
    for field in obj_data:
        if field in update_data:
            setattr(db_obj, field, update_data[field])
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj
    
#Statuses
def get_all_statuses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Status).offset(skip).limit(limit).all()

def get_status(db: Session, status_id: int):
    return db.query(models.Status).filter(models.Status.id == status_id).first()

def get_status_name(db: Session, status_name: str):
    return db.query(models.Status).filter(models.Status.status_name == status_name).first()

def post_status(db: Session, status: schemas.StatusCreate):
    status = models.Status(status_name = status.status_name)
    db.add(status)
    db.commit()
    db.refresh(status)
    return status

def delete_status(db: Session, status_id: int):
    status_to_delete = db.query(models.Status).filter(models.Status.id == status_id).first()
    db.delete(status_to_delete)
    db.commit()
    return schemas.ResponseModel(details=f"Status {status_id} has been deleted")

def put_status(db: Session, db_obj, obj_in):
    obj_data = jsonable_encoder(db_obj)
    if isinstance(obj_in, dict):
        update_data = obj_in
    else:
        update_data = obj_in.dict(exclude_unset=True)
    for field in obj_data:
        if field in update_data:
            setattr(db_obj, field, update_data[field])
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

#Levels
def get_all_levels(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Level).offset(skip).limit(limit).all()

def get_level(db: Session, level_id: int):
    return db.query(models.Level).filter(models.Level.id == level_id).first()

def get_level_name(db: Session, level_name: str):
    return db.query(models.Level).filter(models.Level.level_name == level_name).first()

def post_level(db: Session, level: schemas.LevelCreate):
    level = models.Level(level_name = level.level_name)
    db.add(level)
    db.commit()
    db.refresh(level)
    return level

def delete_level(db: Session, level_id: int):
    level_to_delete = db.query(models.Level).filter(models.Level.id == level_id).first()
    db.delete(level_to_delete)
    db.commit()
    return schemas.ResponseModel(details=f"Status {level_id} has been deleted")

def put_level(db: Session, db_obj, obj_in):
    obj_data = jsonable_encoder(db_obj)
    if isinstance(obj_in, dict):
        update_data = obj_in
    else:
        update_data = obj_in.dict(exclude_unset=True)
    for field in obj_data:
        if field in update_data:
            setattr(db_obj, field, update_data[field])
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

#TicketTypes
def get_all_ticket_types(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.TicketType).offset(skip).limit(limit).all()

def get_ticket_type(db: Session, ticket_type_id: int):
    return db.query(models.TicketType).filter(models.TicketType.id == ticket_type_id).first()

def get_ticket_type_name(db: Session, ticket_type_name: str):
    return db.query(models.TicketType).filter(models.TicketType.ticket_type_name == ticket_type_name).first()

def post_ticket_type(db: Session, ticket_type: schemas.TicketTypeCreate):
    ticket_type = models.TicketType(ticket_type_name = ticket_type.ticket_type_name)
    db.add(ticket_type)
    db.commit()
    db.refresh(ticket_type)
    return ticket_type

def delete_ticket_type(db: Session, ticket_type_id: int):
    ticket_type_to_delete = db.query(models.TicketType).filter(models.TicketType.id == ticket_type_id).first()
    db.delete(ticket_type_to_delete)
    db.commit()
    return schemas.ResponseModel(details=f"Ticket type {ticket_type_id} has been deleted")

def put_ticket_type(db: Session, db_obj, obj_in):
    obj_data = jsonable_encoder(db_obj)
    if isinstance(obj_in, dict):
        update_data = obj_in
    else:
        update_data = obj_in.dict(exclude_unset=True)
    for field in obj_data:
        if field in update_data:
            setattr(db_obj, field, update_data[field])
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj