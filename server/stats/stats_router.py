from fastapi import APIRouter
from stats.stats_repo import read_players_from_file

router = APIRouter(
    prefix="/stats"
)


@router.get("/")
async def get_players():
    players = await read_players_from_file()
    return {"players": players}
