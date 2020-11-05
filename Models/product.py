"""Script creating the tables, using the SQLAlchemy ORM."""
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from base import Base

class Product(Base):
    __tablename__ = "Product"

    Id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(100), nullable=False)
    quantity = Column(String(40), nullable=False)
    id_category = Column(Integer, ForeignKey("Category.Id"), nullable=False)
    nutri_score = Column(String(1), nullable=False)
    ingredients = Column(String(1000), nullable=False)
    link_url = Column(String(100), nullable=False)

    category = relationship("Category", backref="Product")
