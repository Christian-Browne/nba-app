from pydantic import BaseModel
from enum import Enum


class PlayerIn(BaseModel):
    first_name: str
    last_name: str
    number: int
    position: str
    nickname: str
    image: str


class Position(str, Enum):
    point_guard = "point guard"

