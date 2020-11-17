"""Script creating the tables, using the SQLAlchemy ORM."""
from sqlalchemy import Column, Integer, String
from Models.base import Base


class Category(Base):
    __tablename__ = "Category"

    Id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
