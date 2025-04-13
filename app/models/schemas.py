from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    balance: float
    
    class Config:
        orm_mode = True

class EventBase(BaseModel):
    name: str
    game: str
    team_a: str
    team_b: str
    odds_a: float
    odds_b: float
    start_time: datetime

class EventCreate(EventBase):
    pass

class EventUpdate(BaseModel):
    status: Optional[str] = None
    winner: Optional[str] = None
    end_time: Optional[datetime] = None

class Event(EventBase):
    id: int
    status: str
    winner: Optional[str] = None
    end_time: Optional[datetime] = None
    
    class Config:
        orm_mode = True

class BetBase(BaseModel):
    event_id: int
    amount: float
    team: str  # team_a or team_b

class BetCreate(BetBase):
    pass

class Bet(BetBase):
    id: int
    user_id: int
    odds: float
    placed_at: datetime
    status: str
    potential_payout: float
    
    class Config:
        orm_mode = True 