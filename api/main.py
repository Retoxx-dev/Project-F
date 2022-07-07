from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from fastapi.middleware.cors import CORSMiddleware

from . import crud, models, schemas, oauth2, token_gen, seed
from .database import SessionLocal, engine

from contextlib import contextmanager
from fastapi.concurrency import contextmanager_in_threadpool

app = FastAPI(
    swagger_ui_parameters={"defaultModelsExpandDepth": -1}
)

models.Base.metadata.create_all(bind=engine)

origins = [
    "http://localhost",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
 
#Seed
@app.on_event("startup")
async def configure():
    async with contextmanager_in_threadpool(contextmanager(get_db)()) as db:
        seed.seed_initial_data(db=db)
    
#Auth
@app.post('/api/auth/', tags=["Authorize"])
def authorize(auth: schemas.Auth, db: Session = Depends(get_db)):
    user = crud.verify_email(db=db, email=auth.email)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    verify_password = crud.verify_password(db=db, password=auth.password, hashed_password=user.password_hash)
    if not verify_password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    access_token = token_gen.create_access_token(data={"sub": user.email})
    
    return {'access_token' : access_token}

#Tickets
@app.get('/api/tickets/', response_model=list[schemas.Ticket], tags=["Tickets"])
def read_all_tickets(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), get_current_user: schemas.Agent = Depends(oauth2.get_current_user)):
    all_tickets = crud.get_all_tickets(db, skip=skip, limit=limit)
    return all_tickets

@app.get("/api/tickets/{ticket_id}", response_model=schemas.Ticket, tags=["Tickets"])
def read_ticket(ticket_id: int, db: Session = Depends(get_db), get_current_user: schemas.Agent = Depends(oauth2.get_current_user)):
    ticket = crud.get_ticket(db, ticket_id=ticket_id)
    if ticket is None:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return ticket

@app.post("/api/tickets/", response_model=schemas.TicketNoJoin, tags=["Tickets"]) # fix response model
def create_ticket(ticket: schemas.TicketCreate, db: Session = Depends(get_db), get_current_user: schemas.Agent = Depends(oauth2.get_current_user)):
    check_for_status = crud.get_status(db=db, status_id=ticket.status_id)
    if not check_for_status:
        raise HTTPException(status_code=404, detail="Status with that ID wasn't found")
    check_for_level = crud.get_level(db=db, level_id=ticket.level_id)
    if not check_for_level:
        raise HTTPException(status_code=404, detail="Level with that ID wasn't found")
    check_for_ticket_type = crud.get_ticket_type(db=db, ticket_type_id=ticket.ticket_type_id)
    if not check_for_ticket_type:
        raise HTTPException(status_code=404, detail="Ticket Type with that ID wasn't found")
    check_for_customer = crud.get_customer(db=db, customer_id=ticket.customer_id)
    if not check_for_customer:
        raise HTTPException(status_code=404, detail="Customer with that ID wasn't found")
    check_for_agent = crud.get_agent(db=db, agent_id=ticket.agent_id)
    if not check_for_agent:
        raise HTTPException(status_code=404, detail="Agent with that ID wasn't found")
    return crud.post_ticket(db=db, ticket=ticket)

@app.delete("/api/tickets/{ticket_id}", response_model=schemas.ResponseModel, tags=["Tickets"])
def delete_ticket(ticket_id: int, db: Session = Depends(get_db), get_current_user: schemas.Agent = Depends(oauth2.get_current_user)):
    ticket = crud.get_ticket(db, ticket_id=ticket_id)
    if not ticket:
        raise HTTPException(status_code=404, detail=f"Ticket not found")
    return crud.delete_ticket(db=db, ticket_id=ticket_id)

@app.put("/api/tickets/{ticket_id}", response_model=schemas.TicketNoJoin ,tags=["Tickets"]) #fix response model
def update_ticket(ticket_id: int, ticket: schemas.TicketUpdate, db: Session = Depends(get_db), get_current_user: schemas.Agent = Depends(oauth2.get_current_user)):
    check_for_status = crud.get_status(db=db, status_id=ticket.status_id)
    if not check_for_status and ticket.status_id is not None:
        raise HTTPException(status_code=404, detail="Status with that ID wasn't found")
    check_for_level = crud.get_level(db=db, level_id=ticket.level_id)
    if not check_for_level and ticket.level_id is not None:
        raise HTTPException(status_code=404, detail="Level with that ID wasn't found")
    check_for_ticket_type = crud.get_ticket_type(db=db, ticket_type_id=ticket.ticket_type_id)
    if not check_for_ticket_type and ticket.ticket_type_id is not None:
        raise HTTPException(status_code=404, detail="Ticket Type with that ID wasn't found")
    check_for_customer = crud.get_customer(db=db, customer_id=ticket.customer_id)
    if not check_for_customer and ticket.customer_id is not None:
        raise HTTPException(status_code=404, detail="Customer with that ID wasn't found")
    check_for_agent = crud.get_agent(db=db, agent_id=ticket.agent_id)
    if not check_for_agent and ticket.agent_id is not None:
        raise HTTPException(status_code=404, detail="Agent with that ID wasn't found")
    db_ticket = crud.get_ticket_no_join(db, ticket_id=ticket_id)
    if db_ticket:
        db_ticket = crud.put_ticket(db=db, db_obj=db_ticket, obj_in=ticket)
        return db_ticket
    raise HTTPException(status_code=404, detail="Ticket not found")
        
#Statuses
@app.get('/api/statuses/', response_model=list[schemas.Status], tags=["Statuses"])
def read_all_statuses(skip: int = 0, limit: int=100, db: Session = Depends(get_db), get_current_user: schemas.Agent = Depends(oauth2.get_current_user)):
    all_statuses = crud.get_all_statuses(db, skip=skip, limit=limit)
    return all_statuses

@app.get("/api/statuses/{status_id}", response_model=schemas.Status, tags=["Statuses"])
def read_status(status_id: int, db: Session = Depends(get_db), get_current_user: schemas.Agent = Depends(oauth2.get_current_user)):
    status = crud.get_status(db, status_id=status_id)
    if status is None:
        raise HTTPException(status_code=404, detail="Status not found")
    return status

@app.post("/api/statuses/", response_model=schemas.Status, tags=["Statuses"])
def create_status(status: schemas.StatusCreate, db: Session = Depends(get_db), get_current_user: schemas.Agent = Depends(oauth2.get_current_user)):
    db_status = crud.get_status_name(db, status_name=status.status_name)
    if db_status:
        raise HTTPException(status_code=409, detail="Status with that name already exists")
    return crud.post_status(db=db, status=status)

@app.delete("/api/statuses/{status_id}", response_model=schemas.ResponseModel, tags=["Statuses"])
def delete_ticket(status_id: int, db: Session = Depends(get_db), get_current_user: schemas.Agent = Depends(oauth2.get_current_user)):
    status = crud.get_status(db, status_id==status_id)
    if not status:
        raise HTTPException(status_code=404, detail=f"Status not found")
    return crud.delete_status(db=db, status_id=status_id)

@app.put("/api/statuses/{status_id}", response_model=schemas.Status, tags=["Statuses"])
def update_status(status_id: int, status: schemas.StatusUpdate, db: Session = Depends(get_db), get_current_user: schemas.Agent = Depends(oauth2.get_current_user)):
    db_status = crud.get_status(db, status_id=status_id)
    if db_status:
        db_status = crud.put_status(db=db, db_obj=db_status, obj_in=status)
        return db_status
    raise HTTPException(status_code=404, detail="Status not found")


#Levels
@app.get('/api/levels/', response_model=list[schemas.Level], tags=["Levels"])
def read_all_levels(skip: int = 0, limit: int=100, db: Session = Depends(get_db), get_current_user: schemas.Agent = Depends(oauth2.get_current_user)):
    all_levels = crud.get_all_levels(db, skip=skip, limit=limit)
    return all_levels

@app.get("/api/levels/{level_id}", response_model=schemas.Level, tags=["Levels"])
def read_level(level_id: int, db: Session = Depends(get_db), get_current_user: schemas.Agent = Depends(oauth2.get_current_user)):
    level = crud.get_level(db, level_id=level_id)
    if level is None:
        raise HTTPException(status_code=404, detail="Level not found")
    return level

@app.post("/api/levels/", response_model=schemas.Level, tags=["Levels"])
def create_level(level: schemas.LevelCreate, db: Session = Depends(get_db), get_current_user: schemas.Agent = Depends(oauth2.get_current_user)):
    db_level = crud.get_level_name(db, level_name=level.level_name)
    if db_level:
        raise HTTPException(status_code=409, detail="Level with that name already exists")
    return crud.post_level(db=db, level=level)

@app.delete("/api/levels/{level_id}", response_model=schemas.ResponseModel, tags=["Levels"])
def delete_level(level_id: int, db: Session = Depends(get_db), get_current_user: schemas.Agent = Depends(oauth2.get_current_user)):
    level = crud.get_level(db, level_id==level_id)
    if not level:
        raise HTTPException(status_code=404, detail=f"Level not found")
    return crud.delete_level(db=db, level_id=level_id)

@app.put("/api/levels/{level_id}", response_model=schemas.Level, tags=["Levels"])
def update_level(level_id: int, level: schemas.LevelUpdate, db: Session = Depends(get_db), get_current_user: schemas.Agent = Depends(oauth2.get_current_user)):
    db_level = crud.get_level(db, level_id=level_id)
    if db_level:
        db_level = crud.put_level(db=db, db_obj=db_level, obj_in=level)
        return db_level
    raise HTTPException(status_code=404, detail="Level not found")


#TicketTypes
@app.get('/api/tickettypes/', response_model=list[schemas.TicketType], tags=["Ticket Types"])
def read_all_ticket_types(skip: int = 0, limit: int=100, db: Session = Depends(get_db), get_current_user: schemas.Agent = Depends(oauth2.get_current_user)):
    all_ticket_types = crud.get_all_ticket_types(db, skip=skip, limit=limit)
    return all_ticket_types

@app.get("/api/tickettypes/{ticket_type_id}", response_model=schemas.TicketType, tags=["Ticket Types"])
def read_level(ticket_type_id: int, db: Session = Depends(get_db), get_current_user: schemas.Agent = Depends(oauth2.get_current_user)):
    ticket_type = crud.get_ticket_type(db, ticket_type_id=ticket_type_id)
    if ticket_type is None:
        raise HTTPException(status_code=404, detail="Ticket type not found")
    return ticket_type

@app.post("/api/tickettypes/", response_model=schemas.TicketType, tags=["Ticket Types"])
def create_ticket_type(ticket_type: schemas.TicketTypeCreate, db: Session = Depends(get_db), get_current_user: schemas.Agent = Depends(oauth2.get_current_user)):
    db_ticket_type = crud.get_ticket_type_name(db, ticket_type_name=ticket_type.ticket_type_name)
    if db_ticket_type:
        raise HTTPException(status_code=409, detail="Ticket type with that name already exists")
    return crud.post_ticket_type(db=db, ticket_type=ticket_type)

@app.delete("/api/tickettypes/{ticket_type_id}", response_model=schemas.ResponseModel, tags=["Ticket Types"])
def delete_ticket_type(ticket_type_id: int, db: Session = Depends(get_db), get_current_user: schemas.Agent = Depends(oauth2.get_current_user)):
    ticket_type = crud.get_ticket_type(db, ticket_type_id==ticket_type_id)
    if not ticket_type:
        raise HTTPException(status_code=404, detail=f"Ticket type not found")
    return crud.delete_ticket_type(db=db, ticket_type_id=ticket_type_id)

@app.put("/api/tickettypes/{ticket_type_id}", response_model=schemas.TicketType, tags=["Ticket Types"])
def update_level(ticket_type_id: int, ticket_type: schemas.TicketTypeUpdate, db: Session = Depends(get_db), get_current_user: schemas.Agent = Depends(oauth2.get_current_user)):
    db_ticket_type = crud.get_ticket_type(db, ticket_type_id=ticket_type_id)
    if db_ticket_type:
        db_ticket_type = crud.put_ticket_type(db=db, db_obj=db_ticket_type, obj_in=ticket_type)
        return db_ticket_type
    raise HTTPException(status_code=404, detail="Ticket type not found")

#Agents
@app.get('/api/agents/', response_model=list[schemas.Agent], tags=["Agents"])
def read_all_agents(skip: int = 0, limit: int=100, db: Session = Depends(get_db), get_current_user: schemas.Agent = Depends(oauth2.get_current_user)):
    all_agents = crud.get_all_agents(db, skip=skip, limit=limit)
    return all_agents

@app.get("/api/agents/{agent_id}", response_model=schemas.Agent, tags=["Agents"])
def read_agent(agent_id: int, db: Session = Depends(get_db), get_current_user: schemas.Agent = Depends(oauth2.get_current_user)):
    agent = crud.get_agent(db, agent_id=agent_id)
    if agent is None:
        raise HTTPException(status_code=404, detail="Agent not found")
    return agent

@app.post('/api/agents/', response_model=schemas.Agent, tags=["Agents"])
def create_agent(agent: schemas.AgentCreate, db: Session = Depends(get_db), get_current_user: schemas.Agent = Depends(oauth2.get_current_user)):
    agent_db = crud.get_agent_email(db, agent_email=agent.email)
    if agent_db:
        raise HTTPException(status_code=409, detail="Email already taken")
    return crud.post_agent(db=db, agent=agent)

@app.delete("/api/agents/{agent_id}", response_model=schemas.ResponseModel, tags=["Agents"])
def delete_agent(agent_id: int, db: Session = Depends(get_db), get_current_user: schemas.Agent = Depends(oauth2.get_current_user)):
    agent = crud.get_agent(db, agent_id==agent_id)
    if not agent:
        raise HTTPException(status_code=404, detail=f"Agent not found")
    return crud.delete_agent(db=db, agent_id=agent_id)

@app.put("/api/agents/{agent_id}", response_model=schemas.Agent, tags=["Agents"])
def update_agent(agent_id: int, agent: schemas.AgentUpdate, db: Session = Depends(get_db), get_current_user: schemas.Agent = Depends(oauth2.get_current_user)):
    db_agent = crud.get_agent(db, agent_id=agent_id)
    if db_agent:
        db_agent = crud.put_agent(db=db, db_obj=db_agent, obj_in=agent)
        return db_agent
    raise HTTPException(status_code=404, detail="Agent not found")

#Customers
@app.get('/api/customers/', response_model=list[schemas.Customer], tags=["Customers"])
def read_all_customers(skip: int = 0, limit: int=100, db: Session = Depends(get_db), get_current_user: schemas.Agent = Depends(oauth2.get_current_user)):
    all_customers = crud.get_all_customers(db, skip=skip, limit=limit)
    return all_customers

@app.get("/api/customers/{customer_id}", response_model=schemas.Customer, tags=["Customers"])
def read_customer(customer_id: int, db: Session = Depends(get_db), get_current_user: schemas.Agent = Depends(oauth2.get_current_user)):
    customer = crud.get_customer(db, customer_id=customer_id)
    if customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer

@app.post('/api/customers/', response_model=schemas.Customer, tags=["Customers"])
def create_customer(customer: schemas.CustomerCreate, db: Session = Depends(get_db), get_current_user: schemas.Agent = Depends(oauth2.get_current_user)):
    return crud.post_customer(db=db, customer=customer)

@app.delete("/api/customers/{customer_id}", response_model=schemas.ResponseModel, tags=["Customers"])
def delete_customer(customer_id: int, db: Session = Depends(get_db), get_current_user: schemas.Agent = Depends(oauth2.get_current_user)):
    customer = crud.get_customer(db, customer_id=customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail=f"Customer not found")
    return crud.delete_customer(db=db, customer_id=customer_id)

@app.put("/api/customers/{customer_id}", response_model=schemas.Customer, tags=["Customers"])
def update_agent(customer_id: int, customer: schemas.CustomerUpdate, db: Session = Depends(get_db), get_current_user: schemas.Agent = Depends(oauth2.get_current_user)):
    db_customer = crud.get_customer(db, customer_id=customer_id)
    if db_customer:
        db_customer = crud.put_agent(db=db, db_obj=db_customer, obj_in=customer)
        return db_customer
    raise HTTPException(status_code=404, detail="Customer not found")

#Password reset for agents
@app.put('/api/agents/{agent_id}/password', response_model=schemas.ResponseModel, tags=["Agents"])
def reset_password_agent(agent_id: int, agent: schemas.AgentResetPassword, db: Session = Depends(get_db), get_current_user: schemas.Agent = Depends(oauth2.get_current_user)):
    db_agent = crud.get_agent(db, agent_id=agent_id)
    if db_agent:
        if agent.password != agent.confirm_password:
            raise HTTPException(status_code=401, detail="Passwords do not match")
        db_agent =  crud.reset_password_agent(db=db, agent_id=agent_id, agent=agent)
        return {"details" : "Password has been changed"}
    raise HTTPException(status_code=404, detail="Agent not found")

    
        