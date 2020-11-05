"""Script creating the tables, using the SQLAlchemy ORM."""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.base import Base


class Category(Base):
    __tablename__ = "Category"

    Id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(50), nullable=False)

    product = relationship("Product")
