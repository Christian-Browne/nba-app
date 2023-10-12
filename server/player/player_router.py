from fastapi import APIRouter, HTTPException
from player import player_service
from player.player_model import PlayerIn
from player.player_service import PlayerCreationError

router = APIRouter(prefix="/players")


@router.get("/all")
async def get_players():
    try:
        players = await player_service.get_all_players()
        return {"status": "success", "data": players}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.post("/add")
async def add_player(player: PlayerIn):
    try:
        player_id = await player_service.add_player(player)
        return {"status": "success", "data": player_id}
    except PlayerCreationError as e:
        raise HTTPException(status_code=400, detail=str(e))

