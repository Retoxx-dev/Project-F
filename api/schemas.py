from pydantic import BaseModel
from datetime import datetime

class Ticket(BaseModel):
    id: int
    summary: str
    description: str
    username: str
    status_id: int
    level_id: int
    ticket_type_id: int
    date_occured: datetime
    closure_note: str | None = None
    
    class Config:
        orm_mode = True
        
class Status(BaseModel):
    id: int
    status_name: str
    
    class Config:
        orm_mode = True
        
class Level(BaseModel):
    id: int
    level_name: str
    
    class Config:
        orm_mode = True

class TicketType(BaseModel):
    id: int
    ticket_type_name: str
    
    class Config:
        orm_mode = True
        
