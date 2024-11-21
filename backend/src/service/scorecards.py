from src.model.scorecard import Scorecard
from ..data import scorecards


async def get_scorecards():
    return scorecards.get_scorecards()

async def create_scorecard(scorecard: Scorecard):
    try:
        scorecards.create_scorecard(scorecard.playerName, scorecard.playerScore, scorecard.playerStatistics)
        return {
            "message": "Scorecard created successfully",
            "score": scorecard.playerScore
        }
    except Exception as e:
        return {"message": str(e)}