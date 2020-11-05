import json
from ormcreation import Category, Product, Store, Favorite, Junction
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from base import Base, eng

def main():
    for Table in (Favorite, Store, Junction, Product, Category):
        Table.__table__.drop(eng)

if __name__ == "__main__":
    main()