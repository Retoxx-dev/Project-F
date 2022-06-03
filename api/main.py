from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#Tickets
@app.get('/tickets/', response_model=list[schemas.Ticket])
def read_all_tickets(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    all_tickets = crud.get_all_tickets(db, skip=skip, limit=limit)
    return all_tickets

@app.get("/tickets/{ticket_id}", response_model=schemas.Ticket)
def read_ticket(ticket_id: int, db: Session = Depends(get_db)):
    ticket = crud.get_ticket(db, ticket_id=ticket_id)
    if ticket is None:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return ticket

#Statuses
@app.get('/statuses/', response_model=list[schemas.Status])
def read_all_statuses(skip: int = 0, limit: int=100, db: Session = Depends(get_db)):
    all_statuses = crud.get_all_statuses(db, skip=skip, limit=limit)
    return all_statuses

@app.get("/statuses/{status_id}", response_model=schemas.Status)
def read_status(status_id: int, db: Session = Depends(get_db)):
    status = crud.get_status(db, status_id=status_id)
    if status is None:
        raise HTTPException(status_code=404, detail="Status not found")
    return status


#Levels
@app.get('/levels/', response_model=list[schemas.Level])
def read_all_levels(skip: int = 0, limit: int=100, db: Session = Depends(get_db)):
    all_levels = crud.get_all_levels(db, skip=skip, limit=limit)
    return all_levels

@app.get("/levels/{level_id}", response_model=schemas.Level)
def read_level(level_id: int, db: Session = Depends(get_db)):
    level = crud.get_level(db, level_id=level_id)
    if level is None:
        raise HTTPException(status_code=404, detail="Level not found")
    return level


#TicketTypes
@app.get('/tickettypes/', response_model=list[schemas.TicketType])
def read_all_ticket_types(skip: int = 0, limit: int=100, db: Session = Depends(get_db)):
    all_ticket_types = crud.get_all_ticket_types(db, skip=skip, limit=limit)
    return all_ticket_types

@app.get("/tickettypes/{ticket_type_id}", response_model=schemas.TicketType)
def read_level(ticket_type_id: int, db: Session = Depends(get_db)):
    ticket_type = crud.get_ticket_type(db, ticket_type_id=ticket_type_id)
    if ticket_type is None:
        raise HTTPException(status_code=404, detail="Ticket type not found")
    return ticket_type



    
