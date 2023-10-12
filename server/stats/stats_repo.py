import aiofiles


async def read_players_from_file():
    players = []
    try:
        async with aiofiles.open('/database/lakers.txt') as f:
            line = await f.readline()
            while line:
                players.append(line.strip())
                line = await f.readline()
            return players
    except FileNotFoundError as e:
        print(e)

