from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.models.database import get_db, Bet, User, Event
from app.models.schemas import BetCreate, Bet as BetSchema

router = APIRouter(
    prefix="/bets",
    tags=["bets"],
)

@router.post("/", response_model=BetSchema)
def place_bet(bet: BetCreate, user_id: int, db: Session = Depends(get_db)):
    # Check if user exists
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Check if event exists and is upcoming
    event = db.query(Event).filter(Event.id == bet.event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    
    if event.status != "upcoming":
        raise HTTPException(status_code=400, detail="Cannot bet on events that are not upcoming")
    
    # Check if user has enough balance
    if user.balance < bet.amount:
        raise HTTPException(status_code=400, detail="Insufficient balance")
    
    # Check if team is valid
    if bet.team not in ["team_a", "team_b"]:
        raise HTTPException(status_code=400, detail="Team must be 'team_a' or 'team_b'")
    
    # Get odds based on selected team
    odds = event.odds_a if bet.team == "team_a" else event.odds_b
    
    # Calculate potential payout
    potential_payout = bet.amount * odds
    
    # Create bet
    new_bet = Bet(
        user_id=user_id,
        event_id=bet.event_id,
        amount=bet.amount,
        team=bet.team,
        odds=odds,
        potential_payout=potential_payout,
    )
    
    # Deduct amount from user balance
    user.balance -= bet.amount
    
    db.add(new_bet)
    db.commit()
    db.refresh(new_bet)
    
    return new_bet

@router.get("/user/{user_id}", response_model=List[BetSchema])
def get_user_bets(user_id: int, status: str = None, db: Session = Depends(get_db)):
    # Check if user exists
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Query bets
    query = db.query(Bet).filter(Bet.user_id == user_id)
    if status:
        query = query.filter(Bet.status == status)
    
    bets = query.all()
    return bets

@router.get("/event/{event_id}", response_model=List[BetSchema])
def get_event_bets(event_id: int, db: Session = Depends(get_db)):
    # Check if event exists
    event = db.query(Event).filter(Event.id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    
    # Query bets
    bets = db.query(Bet).filter(Bet.event_id == event_id).all()
    return bets 