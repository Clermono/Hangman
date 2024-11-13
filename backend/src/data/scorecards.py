import sqlite3
from src.model.scorecard import Scorecard

DB_NAME = "scorecards.db"
conn = sqlite3.connect(DB_NAME)
curs = conn.cursor()

def init():
    curs.execute(
        """
        CREATE TABLE IF NOT EXISTS scorecards (
            playerId INTEGER PRIMARY KEY AUTOINCREMENT,
            playerName TEXT NOT NULL,
            playerScore INTEGER NOT NULL,
            playerStatistics TEXT
        )
        """
    )

def row_to_scorecard(row: tuple) -> Scorecard:
    playerName, playerScore, playerStatistics = row

    return Scorecard(
        playerName = playerName,
        playerScore = playerScore,
        playerStatistics = playerStatistics
    )

def scorecard_to_dict(scorecard: Scorecard) -> dict:
    return scorecard.model_dump()

def get_scorecards() -> list[Scorecard]:
    curs.execute("SELECT * FROM scorecards")
    rows = list(curs.fetchall())

    return [row_to_scorecard(row) for row in rows]

def create_scorecard(playerName: str, playerScore: int, playerStatistics: dict) -> None:
    curs.execute(
        """
        INSERT INTO scorecards VALUES ()
        """
    )