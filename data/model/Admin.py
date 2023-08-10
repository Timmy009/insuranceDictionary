from typing import List

from pydantic import BaseModel

from data.model.Word import Word


class Admin(BaseModel):
    id: int
    username: str
    password: str
    words: List[Word] = []
