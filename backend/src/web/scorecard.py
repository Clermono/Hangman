from fastapi import APIRouter
from src.model.scorecard import Scorecard
from ..mock import scorecards

router = APIRouter(prefix="/scorecards")


@router.get("")
async def get_scorecards():
    return scorecards.get_scorecards()

@router.post("")
async def create_scorecard(scorecard: Scorecard):
    try:
        scorecards.create_scorecard(scorecard.playerName, scorecard.playerScore, scorecard.playerStatistics)
        return {
            "message": "Scorecard created successfully",
            "score": scorecard.playerScore
        }
    except Exception as e:
        return {"message": str(e)}