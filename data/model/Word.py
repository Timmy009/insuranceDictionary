from typing import List

from pydantic import BaseModel


class Word(BaseModel):
    id: int
    title: str
    meaning: str
    # antonyms: List
    # synonyms: List[str] = []
    # case_study: List[str] = []

    class Config:
        from_attributes = True
