import aiosqlite

DB_NAME = 'database/nba_app.db'


async def fetch_all_players():
    async with aiosqlite.connect(DB_NAME) as db:
        db.row_factory = aiosqlite.Row
        async with db.cursor() as cursor:
            query = """
            SELECT first_name, last_name, number, position, nickname, image FROM players;
            """
            await cursor.execute(query)
            result = await cursor.fetchall()

            players = [dict(row) for row in result]
    return players


async def add_new_player(first_name, last_name, nickname, number, position, image):
    async with aiosqlite.connect(DB_NAME) as db:
        async with db.cursor() as cursor:
            query = """
            INSERT INTO players (first_name, last_name, number, position, nickname, image) 
            VALUES (?, ?, ?, ?, ?, ?)
            """
            await cursor.execute(query, (first_name, last_name, nickname, number, position, image))
            await db.commit()
            return cursor.lastrowid
