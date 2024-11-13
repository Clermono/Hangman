from src.model.scorecard import Scorecard

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
            "word": "space",
            "mistakes": 1,
            "time": 70
        }
    ),
    Scorecard(
        playerName="David Lee",
        playerScore=95,
        playerStatistics={
            "word": "steak",
            "mistakes": 0,
            "time": 60
        }
    ),
    Scorecard(
        playerName="Sophia Patel",
        playerScore=75,
        playerStatistics={
            "word": "spear",
            "mistakes": 5,
            "time": 110
        }
    ),
    Scorecard(
        playerName="Oliver Kim",
        playerScore=65,
        playerStatistics={
            "word": "spite",
            "mistakes": 7,
            "time": 130
        }
    ),
    Scorecard(
        playerName="Isabella Taylor",
        playerScore=80,
        playerStatistics={
            "word": "speed",
            "mistakes": 3,
            "time": 90
        }
    )
]


def get_scorecards():
    scorecards.sort(key=lambda x: x.playerScore, reverse=True)
    return scorecards

def create_scorecard(playerName: str, playerScore: int, playerStatistics: dict):
    scorecards.append(Scorecard(
        playerName = playerName,
        playerScore = playerScore,
        playerStatistics = playerStatistics
    ))

    if len(scorecards) > 10:
        scorecards.sort(key=lambda x: x.playerScore, reverse=True)
        scorecards.pop()