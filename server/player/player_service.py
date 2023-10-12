import aiosqlite
from player import player_repo
from player.player_model import PlayerIn


async def get_all_players():
    players = await player_repo.fetch_all_players()
    if not players:
        raise Exception("No players found")
    return players


async def add_player(player: PlayerIn):
    try:
        return await player_repo.add_new_player(
            player.first_name,
            player.last_name,
            player.nickname, player.number,
            player.position,
            player.image
        )
    except aiosqlite.IntegrityError as e:
        raise PlayerCreationError("Failed to create player")


class PlayerCreationError(Exception):
    pass

