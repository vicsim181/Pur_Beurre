"""Script creating the Store table, using the SQLAlchemy ORM."""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from Models.base import Base


class Store(Base):
    __tablename__ = "Store"

    Id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)

    storeproduct = relationship("StoreProduct", cascade="all, delete")
