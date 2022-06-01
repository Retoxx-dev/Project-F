from pydantic import BaseModel

class TicketBase(BaseModel):
    id: int
    
class Ticket(TicketBase):
    email: str
    
    class Config:
        orm_mode = True