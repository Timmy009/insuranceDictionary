from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.sqlite import *

sql_database_url = "mysql://root:root@localhost:3306/first_db"

engine = create_engine(sql_database_url)

# SQLALCHEMY_DATABASE_URL = "mysql:///./dictionary.db"
#
# engine = create_engine('mysql+root://user:password@localhost/test')

session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


class Words(Base):
    __tablename__ = 'words'

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String(50), unique=True)
    meaning = Column(String(200))


Base.metadata.create_all(bind=engine)
