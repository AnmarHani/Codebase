from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel
import os

Base = declarative_base()

connection_string = "postgresql+psycopg2://" + os.environ['POSTGRES_USER'] + ":" + os.environ["POSTGRES_PASSWORD"] + "@" + os.environ["POSTGRES_HOST"] + ":" + os.environ["POSTGRES_PORT"] + "/" + os.environ["POSTGRES_DB"]
engine = create_engine(connection_string)

class UserTemplate(BaseModel):
    id: int
    name: str
    fullname: str
    nickname: str

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)

    def create(self):
        session.add(self)
        session.commit()

Base.metadata.create_all(engine)

Session = sessionmaker(engine)
session = Session()