import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(50), nullable=False)
    user_name = Column(String(20), nullable=False)
    password = Column(String(10), nullable=False)
    favourites_id = Column(Integer, ForeignKey('favourites.id'))
   
    

class Favourites(Base):
    __tablename__ = 'favourites'
    id = Column(Integer, primary_key=True)
    characters = relationship("characters", backref="favourites")
    planets = relationship("planets", backref="favourites")
    vehicles = relationship("vehicles", backref="favourites")
    user = relationship("user", backref="favourites")
    

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    gender = Column(String)
    hair_color = Column(String)
    eye_color = Column(String)
    favourites_id = Column(Integer, ForeignKey('favourites.id'))
   

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    climate = Column(String)
    gravity = Column(Integer)
    population = Column(Integer)
    favourites_id = Column(Integer, ForeignKey('favourites.id'))
    
    

class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    model = Column(String)
    passengers = Column(Integer)
    speed = Column(Integer)
    favourites_id = Column(Integer, ForeignKey('favourites.id'))
   
  


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')