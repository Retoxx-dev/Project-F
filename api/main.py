from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas, oauth2, token_gen
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
def read_all_tickets(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), get_current_user: schemas.Agent = Depends(oauth2.get_current_user)):
    all_tickets = crud.get_all_tickets(db, skip=skip, limit=limit)
    return all_tickets

@app.get("/tickets/{ticket_id}", response_model=schemas.Ticket)
def read_ticket(ticket_id: int, db: Session = Depends(get_db), get_current_user: schemas.Agent = Depends(oauth2.get_current_user)):
    ticket = crud.get_ticket(db, ticket_id=ticket_id)
    if ticket is None:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return ticket

@app.post("/tickets/", response_model=schemas.Ticket)
def create_ticket(ticket: schemas.TicketCreate, db: Session = Depends(get_db), get_current_user: schemas.Agent = Depends(oauth2.get_current_user)):
    return crud.post_ticket(db=db, ticket=ticket)

@app.delete("/tickets/{ticket_id}", response_model=schemas.ResponseModel)
def delete_ticket(ticket_id: int, db: Session = Depends(get_db), get_current_user: schemas.Agent = Depends(oauth2.get_current_user)):
    ticket = crud.get_ticket(db, ticket_id=ticket_id)
    if not ticket:
        raise HTTPException(status_code=404, detail=f"Ticket not found")
    return crud.delete_ticket(db=db, ticket_id=ticket_id)

@app.put("/tickets/{ticket_id}", response_model=schemas.Ticket)
def update_ticket(ticket_id: int, ticket: schemas.TicketUpdate, db: Session = Depends(get_db), get_current_user: schemas.Agent = Depends(oauth2.get_current_user)):
    db_ticket = crud.get_ticket(db, ticket_id=ticket_id)
    if db_ticket:
        db_ticket = crud.put_ticket(db=db, db_obj=db_ticket, obj_in=ticket)
        return db_ticket
    raise HTTPException(status_code=404, detail="Ticket not found")
        
#Statuses
@app.get('/statuses/', response_model=list[schemas.Status])
def read_all_statuses(skip: int = 0, limit: int=100, db: Session = Depends(get_db), get_current_user: schemas.Agent = Depends(oauth2.get_current_user)):
    all_statuses = crud.get_all_statuses(db, skip=skip, limit=limit)
    return all_statuses

@app.get("/statuses/{status_id}", response_model=schemas.Status)
def read_status(status_id: int, db: Session = Depends(get_db), get_current_user: schemas.Agent = Depends(oauth2.get_current_user)):
    status = crud.get_status(db, status_id=status_id)
    if status is None:
        raise HTTPException(status_code=404, detail="Status not found")
    return status

@app.post("/statuses/", response_model=schemas.Status)
def create_status(status: schemas.StatusCreate, db: Session = Depends(get_db), get_current_user: schemas.Agent = Depends(oauth2.get_current_user)):
    db_status = crud.get_status_name(db, status_name=status.status_name)
    if db_status:
        raise HTTPException(status_code=409, detail="Status with that name already exists")
    return crud.post_status(db=db, status=status)

@app.delete("/statuses/{status_id}", response_model=schemas.ResponseModel)
def delete_ticket(status_id: int, db: Session = Depends(get_db), get_current_user: schemas.Agent = Depends(oauth2.get_current_user)):
    status = crud.get_status(db, status_id==status_id)
    if not status:
        raise HTTPException(status_code=404, detail=f"Status not found")
    return crud.delete_status(db=db, status_id=status_id)

@app.put("/statuses/{status_id}", response_model=schemas.Status)
def update_status(status_id: int, status: schemas.StatusUpdate, db: Session = Depends(get_db), get_current_user: schemas.Agent = Depends(oauth2.get_current_user)):
    db_status = crud.get_status(db, status_id=status_id)
    if db_status:
        db_status = crud.put_status(db=db, db_obj=db_status, obj_in=status)
        return db_status
    raise HTTPException(status_code=404, detail="Status not found")


#Levels
@app.get('/levels/', response_model=list[schemas.Level])
def read_all_levels(skip: int = 0, limit: int=100, db: Session = Depends(get_db), get_current_user: schemas.Agent = Depends(oauth2.get_current_user)):
    all_levels = crud.get_all_levels(db, skip=skip, limit=limit)
    return all_levels

@app.get("/levels/{level_id}", response_model=schemas.Level)
def read_level(level_id: int, db: Session = Depends(get_db), get_current_user: schemas.Agent = Depends(oauth2.get_current_user)):
    level = crud.get_level(db, level_id=level_id)
    if level is None:
        raise HTTPException(status_code=404, detail="Level not found")
    return level

@app.post("/levels/", response_model=schemas.Level)
def create_level(level: schemas.LevelCreate, db: Session = Depends(get_db), get_current_user: schemas.Agent = Depends(oauth2.get_current_user)):
    db_level = crud.get_level_name(db, level_name=level.level_name)
    if db_level:
        raise HTTPException(status_code=409, detail="Level with that name already exists")
    return crud.post_level(db=db, level=level)

@app.delete("/levels/{level_id}", response_model=schemas.ResponseModel)
def delete_level(level_id: int, db: Session = Depends(get_db), get_current_user: schemas.Agent = Depends(oauth2.get_current_user)):
    level = crud.get_level(db, level_id==level_id)
    if not level:
        raise HTTPException(status_code=404, detail=f"Level not found")
    return crud.delete_level(db=db, level_id=level_id)

@app.put("/levels/{level_id}", response_model=schemas.Level)
def update_level(level_id: int, level: schemas.LevelUpdate, db: Session = Depends(get_db), get_current_user: schemas.Agent = Depends(oauth2.get_current_user)):
    db_level = crud.get_level(db, level_id=level_id)
    if db_level:
        db_level = crud.put_level(db=db, db_obj=db_level, obj_in=level)
        return db_level
    raise HTTPException(status_code=404, detail="Level not found")


#TicketTypes
@app.get('/tickettypes/', response_model=list[schemas.TicketType])
def read_all_ticket_types(skip: int = 0, limit: int=100, db: Session = Depends(get_db), get_current_user: schemas.Agent = Depends(oauth2.get_current_user)):
    all_ticket_types = crud.get_all_ticket_types(db, skip=skip, limit=limit)
    return all_ticket_types

@app.get("/tickettypes/{ticket_type_id}", response_model=schemas.TicketType)
def read_level(ticket_type_id: int, db: Session = Depends(get_db), get_current_user: schemas.Agent = Depends(oauth2.get_current_user)):
    ticket_type = crud.get_ticket_type(db, ticket_type_id=ticket_type_id)
    if ticket_type is None:
        raise HTTPException(status_code=404, detail="Ticket type not found")
    return ticket_type

@app.post("/tickettypes/", response_model=schemas.TicketType)
def create_ticket_type(ticket_type: schemas.TicketTypeCreate, db: Session = Depends(get_db), get_current_user: schemas.Agent = Depends(oauth2.get_current_user)):
    db_ticket_type = crud.get_ticket_type_name(db, ticket_type_name=ticket_type.ticket_type_name)
    if db_ticket_type:
        raise HTTPException(status_code=409, detail="Ticket type with that name already exists")
    return crud.post_ticket_type(db=db, ticket_type=ticket_type)

@app.delete("/tickettypes/{ticket_type_id}", response_model=schemas.ResponseModel)
def delete_level(ticket_type_id: int, db: Session = Depends(get_db), get_current_user: schemas.Agent = Depends(oauth2.get_current_user)):
    ticket_type = crud.get_ticket_type(db, ticket_type_id==ticket_type_id)
    if not ticket_type:
        raise HTTPException(status_code=404, detail=f"Ticket type not found")
    return crud.delete_ticket_type(db=db, ticket_type_id=ticket_type_id)

@app.put("/tickettypes/{ticket_type_id}", response_model=schemas.TicketType)
def update_level(ticket_type_id: int, ticket_type: schemas.TicketTypeUpdate, db: Session = Depends(get_db), get_current_user: schemas.Agent = Depends(oauth2.get_current_user)):
    db_ticket_type = crud.get_ticket_type(db, ticket_type_id=ticket_type_id)
    if db_ticket_type:
        db_ticket_type = crud.put_ticket_type(db=db, db_obj=db_ticket_type, obj_in=ticket_type)
        return db_ticket_type
    raise HTTPException(status_code=404, detail="Ticket type not found")

#Users
@app.post('/agents/', response_model=schemas.Agent)
def create_agent(agent: schemas.AgentCreate, db: Session = Depends(get_db), get_current_user: schemas.Agent = Depends(oauth2.get_current_user)):
    return crud.post_agent(db=db, agent=agent)

#Auth
@app.post('/auth/')
def authorize(auth: schemas.Auth, db: Session = Depends(get_db)):
    user = crud.verify_username(db=db, username=auth.username)
    verify_password = crud.verify_password(db=db, password=auth.password, hashed_password=user.password_hash)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    if not verify_password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    access_token = token_gen.create_access_token(data={"sub": user.username})
    
    return {'access_token' : access_token, 'token_type' : 'Bearer'}
    
        