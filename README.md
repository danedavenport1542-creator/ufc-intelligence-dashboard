# ufc-intelligence-dashboard
app/
├── main.py
├── config.py
├── database.py
├── models/
│   ├── fighter.py
│   ├── fight.py
│   ├── fighter_stats.py
│   └── historical_fight.py
├── schemas/
│   ├── fighter.py
│   ├── fight.py
│   └── matchup.py
├── api/v1/
│   ├── fighters.py
│   ├── fights.py
│   ├── matchups.py
│   └── odds.py
├── services/
│   ├── fighter_service.py
│   ├── matchup_service.py
│   ├── data_scraper.py
│   └── prediction_service.py
└── scrapers/
    ├── espn_scraper.py
    ├── sherdog_scraper.py
    └── ufc_scraper.py
# app/models/fighter.py
from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from app.database import Base

class Fighter(Base):
    __tablename__ = "fighters"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    nickname = Column(String, nullable=True)
    fighter_id_espn = Column(String, nullable=True, unique=True)
    fighter_id_sherdog = Column(String, nullable=True, unique=True)
    fighter_id_ufc = Column(String, nullable=True, unique=True)
    
    height_cm = Column(Float, nullable=True)
    weight_lbs = Column(Float, nullable=True)
    reach_inches = Column(Float, nullable=True)
    age = Column(Integer, nullable=True)
    
    wins = Column(Integer, default=0)
    losses = Column(Integer, default=0)
    draws = Column(Integer, default=0)
    
    stance = Column(String, nullable=True)
    division = Column(String, index=True)
    country = Column(String, nullable=True)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
