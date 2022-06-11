from pydantic import BaseModel
from datetime import datetime

from typing import Optional

class ResponseModel(BaseModel):
    details: str

#Ticket
class TicketBase(BaseModel):
    summary: Optional[str] = None
    description: Optional[str] = None
    status_id: Optional[int] = None 
    level_id: Optional[int] = None 
    ticket_type_id: Optional[int] = None 
    closure_note: str | None = None        
  
class TicketCreate(TicketBase):
    summary: str 
    description: str 
    status_id: int 
    level_id: int
    ticket_type_id: int
    closure_note: str | None = None
   
class Ticket(BaseModel): #check if change from TicketBase to BaseModel will to harm
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
        
