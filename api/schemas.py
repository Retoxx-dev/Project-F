from pydantic import BaseModel
from datetime import datetime

#Ticket
class TicketBase(BaseModel):
    pass        
  
class TicketCreate(TicketBase):
    summary: str
    description: str
    username: str
    status_id: int
    level_id: int
    ticket_type_id: int
    closure_note: str | None = None
    
class Ticket(TicketBase):
    id: int
    summary: str
    description: str
    status_id: int
    level_id: int
    ticket_type_id: int
    date_occured: datetime
    closure_note: str | None = None
    
    class Config:
        orm_mode = True
        
#Status
class StatusBase(BaseModel):
    pass        
  
class StatusCreate(StatusBase):
    status_name: str
    
class Status(StatusBase):
    id: int
    status_name: str
    
    class Config:
        orm_mode = True
            
#Level
class LevelBase(BaseModel):
    pass   

class LevelCreate(LevelBase):
    level_name: str

class Level(LevelBase):
    id: int
    level_name: str
    
    class Config:
        orm_mode = True

#TicketType
class TicketTypeBase(BaseModel):
    pass   

class TicketTypeCreate(TicketTypeBase):
    ticket_type_name: str
    
class TicketType(TicketTypeBase):
    id: int
    ticket_type_name: str
    
    class Config:
        orm_mode = True
        
