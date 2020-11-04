"""Script creating the tables, using the SQLAlchemy ORM."""
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

eng = create_engine('mysql://opcr5:japon+72@#cclmvdf@localhost/essai', echo=True)

Base = declarative_base()
 
class Category(Base):
    __tablename__ = "Category"
 
    Id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(50), nullable=False)

    product = relationship("Product")


class Store(Base):
    __tablename__ = "Store"

    Id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(100), nullable=False)


class Favorite(Base):
    __tablename__ = "Favorite"

    Id = Column(Integer, primary_key=True, nullable=False)
    Id_product_replaced = Column(Integer, ForeignKey("Product.Id"), nullable=False)
    Id_product_replacing = Column(Integer, ForeignKey("Product.Id"), nullable=False)


class Product(Base):
    __tablename__ = "Product"

    Id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(100), nullable=False)
    quantity = Column(String(40), nullable=False)
    id_category = Column(Integer, ForeignKey("Category.Id"), nullable=False)
    nutri_score = Column(String(1), nullable=False)
    ingredients = Column(String(500), nullable=False)
    link_url = Column(String(100), nullable=False)

    category = relationship("Category", backref="Product")


class Junction(Base):
    __tablename__ = "Junction_store_product"

    id_product = Column(Integer, ForeignKey("Product.Id"), primary_key=True, nullable=False)
    name_store = Column(String(100))
    id_store = Column(Integer, ForeignKey("Store.Id"), primary_key=True)

    product = relationship("Product")
    store = relationship("Store")

Base.metadata.create_all(eng)