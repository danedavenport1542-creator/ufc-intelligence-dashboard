from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Fight
from app.schemas.matchup import MatchupAnalysis, HistoricalMatchup
from typing import List

router = APIRouter()

@router.get("/{fight_id}/analysis", response_model=MatchupAnalysis)
async def get_matchup_analysis(fight_id: int, db: Session = Depends(get_db)):
    fight = db.query(Fight).filter(Fight.id == fight_id).first()
    if not fight:
        raise HTTPException(status_code=404, detail="Fight not found")
    
    return {
        "fight_id": fight.id,
        "fighter_1_name": fight.fighter_1.name,
        "fighter_2_name": fight.fighter_2.name,
        "ai_prediction_fighter1_win_prob": 0.55,
        "edge_indicator": "Value bet",
        "value_percentage": 0.05,
        "fighter_1_path_to_victory": {
            "fighter_name": fight.fighter_1.name,
            "primary_strategy": "Control striking",
            "key_strengths": ["Striking"],
            "opponent_weaknesses_to_exploit": ["Defense"],
            "confidence": 0.65
        },
        "fighter_2_path_to_victory": {
            "fighter_name": fight.fighter_2.name,
            "primary_strategy": "Takedowns",
            "key_strengths": ["Grappling"],
            "opponent_weaknesses_to_exploit": ["Takedown Defense"],
            "confidence": 0.60
        }
    }

@router.get("/{fight_id}/historical", response_model=List[HistoricalMatchup])
async def get_historical_matchups(fight_id: int, limit: int = 5, db: Session = Depends(get_db)):
    fight = db.query(Fight).filter(Fight.id == fight_id).first()
    if not fight:
        raise HTTPException(status_code=404, detail="Fight not found")
    
    return []

@router.get("/{fight_id}/radar")
async def get_radar_comparison(fight_id: int, db: Session = Depends(get_db)):
    fight = db.query(Fight).filter(Fight.id == fight_id).first()
    if not fight:
        raise HTTPException(status_code=404, detail="Fight not found")
    
    return {
        "fighter_1": {
            "name": fight.fighter_1.name,
            "striking": 75.0,
            "grappling": 65.0,
            "physicals": 70.0,
            "experience": 80.0
        },
        "fighter_2": {
            "name": fight.fighter_2.name,
            "striking": 70.0,
            "grappling": 75.0,
            "physicals": 75.0,
            "experience": 85.0
        }
    }
