"""Script creating the tables, using the SQLAlchemy ORM."""
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import os
from base import Base

class Favorite(Base):
    __tablename__ = "Favorite"

    Id = Column(Integer, primary_key=True, nullable=False)
    Id_product_replaced = Column(Integer, ForeignKey("Product.Id"), nullable=False)
    Id_product_replacing = Column(Integer, ForeignKey("Product.Id"), nullable=False)
