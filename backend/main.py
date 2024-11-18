from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.web import scorecard

app = FastAPI()

app.include_router(scorecard.router)

origins = [
    "http://localhost",
    "http://localhost:5173",
    "http://localhost:5173/scorecards",
    "https://hangman-clermonos-projects.vercel.app",
    "https://hangman-clermonos-projects.vercel.app/scorecards",
    "https://hangman-eight-pi.vercel.app",
    "https://hangman-eight-pi.vercel.app/scorecards",
    "https://hangman-git-master-clermonos-projects.vercel.app",
    "https://hangman-git-master-clermonos-projects.vercel.app/scorecards"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000)