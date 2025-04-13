from sqlalchemy.orm import Session
from app.models.database import Bet, User, Event

def settle_bets_for_event(event_id: int, db: Session) -> int:
    """
    Settle all bets for a completed event
    Returns the number of bets settled
    """
    event = db.query(Event).filter(Event.id == event_id).first()
    if not event or event.status != "completed" or not event.winner:
        return 0
    
    # Get all pending bets for this event
    bets = db.query(Bet).filter(
        Bet.event_id == event_id,
        Bet.status == "pending"
    ).all()
    
    settled_count = 0
    
    for bet in bets:
        user = db.query(User).filter(User.id == bet.user_id).first()
        if not user:
            continue
        
        # Determine if bet won or lost
        if bet.team == event.winner:
            # Win
            bet.status = "won"
            # Pay out winnings
            user.balance += bet.potential_payout
        else:
            # Loss
            bet.status = "lost"
        
        settled_count += 1
    
    db.commit()
    return settled_count 