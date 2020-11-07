"""Script creating the tables, using the SQLAlchemy ORM."""
from sqlalchemy import Column, Integer
from models.base import Base


class StoreProduct(Base):
    __tablename__ = "store_product"

    id_product = Column(Integer, primary_key=True, nullable=False)
    id_store = Column(Integer, primary_key=True)
