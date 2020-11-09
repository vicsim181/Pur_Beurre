"""Script creating the tables, using the SQLAlchemy ORM."""
from sqlalchemy import Column, Integer, ForeignKey
from Models.base import Base


class Favorite(Base):
    __tablename__ = "Favorite"

    Id = Column(Integer, primary_key=True, nullable=False)
    Id_product_replaced = Column(Integer, ForeignKey("Product.Id"),
                                 nullable=False)
    Id_product_replacing = Column(Integer, ForeignKey("Product.Id"),
                                  nullable=False)
