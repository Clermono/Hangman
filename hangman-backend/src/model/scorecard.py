from pydantic import BaseModel


class Scorecard(BaseModel):
    playerName: str
    playerScore: int
    playerStatistics: dict