from .init import conn, curs
from src.model.scorecard import Scorecard

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

scorecards = [
    Scorecard(
        playerName="John Doe",
        playerScore=100,
        playerStatistics={
            "word": "house",
            "mistakes": 5,
            "time": 60
        }
    ),
    Scorecard(
        playerName="Jane Smith",
        playerScore=80,
        playerStatistics={
            "word": "stamp",
            "mistakes": 3,
            "time": 90
        }
    ),
    Scorecard(
        playerName="Bob Johnson",
        playerScore=90,
        playerStatistics={
            "word": "knife",
            "mistakes": 2,
            "time": 80
        }
    ),
    Scorecard(
        playerName="Alice Brown",
        playerScore=70,
        playerStatistics={
            "word": "dance",
            "mistakes": 4,
            "time": 100
        }
    ),
    Scorecard(
        playerName="Mike Davis",
        playerScore=60,
        playerStatistics={
            "word": "flute",
            "mistakes": 6,
            "time": 120
        }
    ),
    Scorecard(
        playerName="Emily Chen",
        playerScore=85,
        playerStatistics={
            "word": "spear",
            "mistakes": 5,
            "time": 110
        }
    ),
    Scorecard(
        playerName="Sophia Patel",
        playerScore=75,
        playerStatistics={
            "word": "spite",
            "mistakes": 7,
            "time": 130
        }
    ),
    Scorecard(
        playerName="Oliver Kim",
        playerScore=65,
        playerStatistics={
            "word": "speed",
            "mistakes": 3,
            "time": 90
        }
    ),
    Scorecard(
        playerName="Isabella Taylor",
        playerScore=80,
        playerStatistics={
            "word": "stamp",
            "mistakes": 3,
            "time": 90
        }
    )
]

for scorecard in scorecards:
    curs.execute(
        """
            INSERT INTO scorecards VALUES (:playerName, :playerScore, :playerStatistics)
        """,
        scorecard.playerName, scorecard.playerScore, str(scorecard.playerStatistics)
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

def create_scorecard(scorecard: Scorecard) -> None:
    qry = """
            INSERT INTO scorecards VALUES (:playerName, :playerScore, :playerStatistics)
        """
    params = scorecard_to_dict(scorecard)

    curs.execute(qry, params)

def delete_worst_scorecard() -> None:
    curs.execute("DELETE FROM scorecards WHERE playerScore = (SELECT MIN(playerScore) FROM scorecards)")