"""Script creating the Favorite table, using the SQLAlchemy ORM."""
from sqlalchemy import Column, Integer, ForeignKey, DateTime
from Models.base import Base


class Favorite(Base):
    __tablename__ = "Favorite"

    Id = Column(Integer, autoincrement=True)
    Id_product_replaced = Column(Integer, ForeignKey("Product.Id", ondelete="CASCADE"), primary_key=True,
                                 nullable=False)
    Id_product_replacing = Column(Integer, ForeignKey("Product.Id", ondelete="CASCADE"), primary_key=True,
                                  nullable=False)
    date_creation = Column(DateTime, nullable=False)
