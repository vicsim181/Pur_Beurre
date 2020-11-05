"""Script creating the tables, using the SQLAlchemy ORM."""
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from base import Base

class StoreProduct(Base):
    __tablename__ = "store_product"

    id_product = Column(Integer, ForeignKey("Product.Id"), primary_key=True, nullable=False)
    name_store = Column(String(100))
    id_store = Column(Integer, primary_key=True)

    product = relationship("Product")
    # store = relationship("Store")

