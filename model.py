from engine import engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))

class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    description = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        return {
            'Id': self.id,
            'Title': self.title,
            'Description': self.description
        }

class Game (Base):
    __tablename__ = 'game'
    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    short_description = Column(String(250), nullable=False)
    long_description = Column(String(250), nullable=False)
    category_id = Column(Integer, ForeignKey('category.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    category = relationship(Category)
    user = relationship(User)
    
    @property
    def serialize(self):
        return {
            'Title': self.title,
            'Short description': self.short_description,
            'Long description': self.long_description,
        }
Base.metadata.create_all(engine)