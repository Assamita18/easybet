from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import uvicorn

from app.models.database import init_db, get_db
from app.routes import users, events, bets
from app.utils.settlement import settle_bets_for_event

app = FastAPI(
    title="EasyBet - E-Sports Betting API",
    description="A simple API for betting on e-sports events",
    version="0.1.0",
)

# Initialize database
@app.on_event("startup")
def startup_event():
    init_db()

# Include routers
app.include_router(users.router)
app.include_router(events.router)
app.include_router(bets.router)

@app.get("/")
def read_root():
    return {
        "message": "Welcome to EasyBet API! Bet on your favorite e-sports events.",
        "documentation": "/docs",
    }

@app.post("/events/{event_id}/settle", tags=["settlement"])
def settle_event(event_id: int, db: Session = Depends(get_db)):
    settled_count = settle_bets_for_event(event_id, db)
    return {"message": f"Settled {settled_count} bets for event {event_id}"}

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True) 