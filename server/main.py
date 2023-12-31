from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from stats import stats_router
from player import player_router

app = FastAPI()

origins = [
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(stats_router.router)
app.include_router(player_router.router)
