from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
from utils.database import engine

Base = declarative_base()
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)

Base.metadata.create_all(engine)