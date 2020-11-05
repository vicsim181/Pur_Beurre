"""Script creating the tables, using the SQLAlchemy ORM."""
from sqlalchemy import Column, Integer, String
from models.base import Base


class Store(Base):
    __tablename__ = "Store"

    Id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(100), nullable=False)
