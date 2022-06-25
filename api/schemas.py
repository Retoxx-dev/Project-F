from pydantic import BaseModel
from datetime import datetime

from typing import Optional

class ResponseModel(BaseModel):
    details: str

#Ticket
class TicketBase(BaseModel):
    summary: Optional[str] = None
    description: Optional[str] = None
    customer_id: Optional[int] = None
    status_id: Optional[int] = None 
    level_id: Optional[int] = None
    agent_id: Optional[int] = None
    ticket_type_id: Optional[int] = None 
    closure_note: str | None = None        
  
class TicketCreate(TicketBase):
    summary: str 
    description: str
    customer_id: int
    status_id: int 
    level_id: int
    agent_id: int
    ticket_type_id: int
    closure_note: str | None = None
   
class Ticket(BaseModel): #check if change from TicketBase to BaseModel will to harm
    id: int
    summary: str
    description: str
    customer_id: int
    customer_username: str
    status_id: int
    status_name: str
    level_id: int
    level_name: str
    agent_id: int
    agent_username: str
    ticket_type_id: int
    ticket_type_name: str
    date_occured: datetime
    closure_note: str | None = None
    
    class Config:
        orm_mode = True
        
class TicketUpdate(TicketBase):
    pass


#Status
class StatusBase(BaseModel):
    status_name: Optional[str] = None     
  
class StatusCreate(StatusBase):
    status_name: str 
    
class Status(BaseModel):
    id: int
    status_name: str
    
    class Config:
        orm_mode = True

class StatusUpdate(StatusBase):
    pass
            
#Level
class LevelBase(BaseModel):
    level_name: Optional[str] = None   

class LevelCreate(LevelBase):
    level_name: str
    
class LevelUpdate(LevelBase):
    pass

class Level(BaseModel):
    id: int
    level_name: str
    
    class Config:
        orm_mode = True

#TicketType
class TicketTypeBase(BaseModel):
    ticket_type_name: Optional[str] = None 

class TicketTypeCreate(TicketTypeBase):
    ticket_type_name: str
    
class TicketTypeUpdate(TicketTypeBase):
    pass
    
class TicketType(BaseModel):
    id: int
    ticket_type_name: str
    
    class Config:
        orm_mode = True
        
#Agent
class AgentBase(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    
class Agent(BaseModel): #check if change from TicketBase to BaseModel will to harm
    id: int
    username: Optional[str] = None
    email: Optional[str] = None
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    
    class Config:
        orm_mode = True

class AgentCreate(AgentBase):
    username: str
    email: str
    firstname: str
    lastname: str
    password: str
        
class AgentUpdate(AgentBase):
    pass

class AgentResetPassword(BaseModel):
    password: str
    confirm_password: str

#Auth
class Auth(BaseModel):
    username: str
    password: str
    
    
#Token
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None
    
#Customers
class CustomerBase(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    
class Customer(BaseModel): #check if change from TicketBase to BaseModel will to harm
    id: int
    username: Optional[str] = None
    email: Optional[str] = None
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    
    class Config:
        orm_mode = True

class CustomerCreate(CustomerBase):
    username: str
    email: str
    firstname: str
    lastname: str
        
class CustomerUpdate(CustomerBase):
    pass
