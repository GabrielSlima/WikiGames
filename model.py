from engine import engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primaryKey=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))

class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primaryKey=True)
    title = Column(String(250), nullable=False)
    description = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey)
    user = relationship(User)

class Game (Base):
    __tablename__ = 'game'
    id = Column(Integer, primaryKey=True)
    title = Column(String(250), nullable=False)
    short_description = Column(String(250), nullable=False)
    long_description = Column(String(250), nullable=False)
    category_id = Column(Integer, ForeignKey)
    user_idColumn(Integer, ForeignKey)
    category = relationship(Category)
    user = relationship(User)