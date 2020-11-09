"""Script creating the tables, using the SQLAlchemy ORM."""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from Models.base import Base


class Product(Base):
    __tablename__ = "Product"

    Id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(100), nullable=False)
    quantity = Column(String(40), nullable=False)
    id_category = Column(Integer, ForeignKey("Category.Id"), nullable=False)
    nutri_score = Column(String(1), nullable=False)
    ingredients = Column(String(10000), nullable=False)
    link_url = Column(String(250), nullable=False)
    stores = Column(String(150))

    category = relationship("Category", backref="Product")
