"""Script creating the StoreProduct table, using the SQLAlchemy ORM."""
from sqlalchemy import Column, Integer, ForeignKey
from Models.base import Base


class StoreProduct(Base):
    __tablename__ = "store_product"

    id_product = Column(Integer, ForeignKey("Product.Id", ondelete="CASCADE"), primary_key=True, nullable=False)
    id_store = Column(Integer, ForeignKey("Store.Id", ondelete="CASCADE"), primary_key=True)
