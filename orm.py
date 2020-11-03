#!/usr/bin/python
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

eng = create_engine('mysql://opcr5:japon+72@#cclmvdf@localhost/essai', echo=True)

Base = declarative_base()
 
class Category(Base):
    __tablename__ = "Categories"
 
    Id = Column(Integer, primary_key=True, nullable=False)
    Name = Column(String(50))


class Store(Base):
    __tablename__ = "Stores"

    Id = Column(Integer, primary_key=True, nullable=False)
    Name = Column(String(100), nullable=False)


class Favorite(Base):
    __tablename__ = "Favorites"

    Id = Column(Integer, primary_key=True, nullable=False)
    Id_product_replaced = Column(Integer, foreign_key)



Base.metadata.create_all(eng)