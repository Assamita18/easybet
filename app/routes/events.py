from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime

from app.models.database import get_db, Event
from app.models.schemas import EventCreate, Event as EventSchema, EventUpdate

router = APIRouter(
    prefix="/events",
    tags=["events"],
)

@router.post("/", response_model=EventSchema)
def create_event(event: EventCreate, db: Session = Depends(get_db)):
    new_event = Event(
        name=event.name,
        game=event.game,
        team_a=event.team_a,
        team_b=event.team_b,
        odds_a=event.odds_a,
        odds_b=event.odds_b,
        start_time=event.start_time,
        status="upcoming"
    )
    db.add(new_event)
    db.commit()
    db.refresh(new_event)
    return new_event

@router.get("/", response_model=List[EventSchema])
def get_events(skip: int = 0, limit: int = 100, status: str = None, db: Session = Depends(get_db)):
    query = db.query(Event)
    if status:
        query = query.filter(Event.status == status)
    events = query.offset(skip).limit(limit).all()
    return events

@router.get("/{event_id}", response_model=EventSchema)
def get_event(event_id: int, db: Session = Depends(get_db)):
    event = db.query(Event).filter(Event.id == event_id).first()
    if event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return event

@router.put("/{event_id}", response_model=EventSchema)
def update_event(event_id: int, event_update: EventUpdate, db: Session = Depends(get_db)):
    db_event = db.query(Event).filter(Event.id == event_id).first()
    if db_event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    
    update_data = event_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_event, key, value)
    
    db.commit()
    db.refresh(db_event)
    return db_event

@router.put("/{event_id}/complete", response_model=EventSchema)
def complete_event(event_id: int, winner: str, db: Session = Depends(get_db)):
    db_event = db.query(Event).filter(Event.id == event_id).first()
    if db_event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    
    if winner not in ["team_a", "team_b", "draw"]:
        raise HTTPException(status_code=400, detail="Winner must be 'team_a', 'team_b', or 'draw'")
    
    db_event.status = "completed"
    db_event.winner = winner
    db_event.end_time = datetime.utcnow()
    
    db.commit()
    db.refresh(db_event)
    return db_event 