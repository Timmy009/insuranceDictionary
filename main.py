from fastapi import FastAPI
from fastapi.params import Depends
from sqlalchemy.orm import Session
from typing_extensions import List

from data.model.Word import Word
from data.repositories.Words import session, Words

app = FastAPI()


def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()


# @app.get("/")
# async def root():
#     return {"message": "Hello World"}
#
#
# @app.get("/hello/{name}")
# async def say_hello(name: str):
#     return {"message": f"Hello {name}"}


@app.post('/add_new', response_model=Word)
def add_book(b1: Word, db: Session = Depends(get_db)):
    bk = Words(id=b1.id, title=b1.title, meaning=b1.author)
    db.add(bk)
    db.commit()
    db.refresh(bk)


@app.get('/list', response_model=List[Word])
def get_books(db: Session = Depends(get_db)):
    recs = db.query(Words).all()
    return recs
