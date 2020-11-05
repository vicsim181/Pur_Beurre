"""Script creating the tables, using the SQLAlchemy ORM."""
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from base import Base

class Store(Base):
    __tablename__ = "Store"

    Id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(100), nullable=False)