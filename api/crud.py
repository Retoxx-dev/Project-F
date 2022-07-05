from sqlalchemy.orm import Session

from . import models, schemas, rabbitmq_producer

from fastapi.encoders import jsonable_encoder

from passlib.hash import bcrypt

#Tickets
def get_ticket(db: Session, ticket_id: int):
    return db.query(models.Ticket.id, models.Ticket.summary, models.Ticket.description, models.Ticket.customer_id,
                    models.Ticket.status_id, models.Ticket.level_id, models.Ticket.agent_id, models.Ticket.ticket_type_id,
                    models.Ticket.date_occured, models.Ticket.closure_note, models.Customer.username.label('customer_username'),
                    models.Status.status_name.label('status_name'), models.Level.level_name.label('level_name'),
                    models.Agent.username.label('agent_username'), models.TicketType.ticket_type_name.label('ticket_type_name')).join(models.Customer, 
                                                                                                                                      models.Status, 
                                                                                                                                      models.Agent,
                                                                                                                                      models.Level,
                                                                                                                                      models.TicketType).filter(models.Ticket.id == ticket_id).first()
    
def get_ticket_no_join(db: Session, ticket_id: int):    
    return db.query(models.Ticket).filter(models.Ticket.id == ticket_id).first()

def get_all_tickets(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Ticket.id, models.Ticket.summary, models.Ticket.description, models.Ticket.customer_id,
                    models.Ticket.status_id, models.Ticket.level_id, models.Ticket.agent_id, models.Ticket.ticket_type_id,
                    models.Ticket.date_occured, models.Ticket.closure_note, models.Customer.username.label('customer_username'),
                    models.Status.status_name.label('status_name'), models.Level.level_name.label('level_name'),
                    models.Agent.username.label('agent_username'), models.TicketType.ticket_type_name.label('ticket_type_name')).join(models.Customer, 
                                                                                                                                      models.Status, 
                                                                                                                                      models.Agent,
                                                                                                                                      models.Level,
                                                                                                                                      models.TicketType).all()

def post_ticket(db: Session, ticket: schemas.TicketCreate):
    ticket = models.Ticket(
        summary = ticket.summary,
        description = ticket.description,
        customer_id = ticket.customer_id,
        status_id = ticket.status_id,
        level_id = ticket.level_id,
        agent_id = ticket.agent_id,
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

#Agents
def get_agent(db: Session, agent_id: int):
    return db.query(models.Agent).filter(models.Agent.id == agent_id).first()

def get_agent_email(db: Session, agent_email):
    return db.query(models.Agent).filter(models.Agent.email == agent_email).first()

def get_all_agents(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Agent).offset(skip).limit(limit).all()

def post_agent(db: Session, agent: schemas.AgentCreate):
    agent = models.Agent(
        username = agent.username,
        email = agent.email,
        firstname = agent.firstname,
        lastname = agent.lastname,
        password_hash = bcrypt.hash(agent.password)
    )
    db.add(agent)
    db.commit()
    db.refresh(agent)
    rabbitmq_producer.send_email(email_recipient=str(agent.email))
    return agent


def delete_agent(db: Session, agent_id: int):
    agent_to_delete = db.query(models.Agent).filter(models.Agent.id == agent_id).first()
    db.delete(agent_to_delete)
    db.commit()
    return schemas.ResponseModel(details=f"Agent {agent_id} has been deleted")

def put_agent(db: Session, db_obj, obj_in):
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

def reset_password_agent(db: Session, agent_id: int, agent: schemas.AgentResetPassword):
    user_password_to_change = db.query(models.Agent).filter(models.Agent.id == agent_id).first()
    new_password_hash = bcrypt.hash(agent.password)
    user_password_to_change.password_hash = new_password_hash
    db.add(user_password_to_change)
    db.commit()
    db.refresh(user_password_to_change)
    return user_password_to_change

#Customers
def get_customer(db: Session, customer_id: int):
    return db.query(models.Customer).filter(models.Customer.id == customer_id).first()

def get_all_customers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Customer).offset(skip).limit(limit).all()

def post_customer(db: Session, customer: schemas.CustomerCreate):
    customer = models.Customer(
        username = customer.username,
        email = customer.email,
        firstname = customer.firstname,
        lastname = customer.lastname
    )
    db.add(customer)
    db.commit()
    db.refresh(customer)
    return customer

def delete_customer(db: Session, customer_id: int):
    customer_to_delete = db.query(models.Customer).filter(models.Customer.id == customer_id).first()
    db.delete(customer_to_delete)
    db.commit()
    return schemas.ResponseModel(details=f"Customer {customer_id} has been deleted")

def put_customer(db: Session, db_obj, obj_in):
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

#Auth
def verify_email(db: Session, email: str):
    return db.query(models.Agent).filter(models.Agent.email == email).first()

def verify_password(db: Session, password: str, hashed_password: str):
    return bcrypt.verify(password, hashed_password)