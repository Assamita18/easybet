from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import datetime
import os

DATABASE_URL = "sqlite:///./app/data/easybet.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    balance = Column(Float, default=100.0)
    bets = relationship("Bet", back_populates="user")

class Event(Base):
    __tablename__ = "events"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    game = Column(String, index=True)
    team_a = Column(String)
    team_b = Column(String)
    odds_a = Column(Float)
    odds_b = Column(Float)
    start_time = Column(DateTime)
    end_time = Column(DateTime, nullable=True)
    status = Column(String, default="upcoming")  # upcoming, live, completed
    winner = Column(String, nullable=True)  # team_a, team_b, draw
    bets = relationship("Bet", back_populates="event")

class Bet(Base):
    __tablename__ = "bets"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    event_id = Column(Integer, ForeignKey("events.id"))
    amount = Column(Float)
    team = Column(String)  # team_a or team_b
    odds = Column(Float)
    placed_at = Column(DateTime, default=datetime.datetime.utcnow)
    status = Column(String, default="pending")  # pending, won, lost
    potential_payout = Column(Float)
    
    user = relationship("User", back_populates="bets")
    event = relationship("Event", back_populates="bets")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    Base.metadata.create_all(bind=engine) 