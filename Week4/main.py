from Fastapi import FastAPI, HTTPException, Depends
from Sqlalchemy import create_engine, column, Integer, String, Float, Foreign_key
from Sqlalchemy.ext.declarative import declarative_base
from Sqlalchemy.orm import sessionmaker,  Session
from pydantic import BaseModel
from typing import List
import datetime
DATABASE_URL = "sqlite:///./orders.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread":False})
SessinLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class ProductTable(Base):
    __tablename__ = "products"
    id = column(Integer, primary_key=True, index=True)
    name = column(String, index=True)
    price = column(float)
    stock = column(Integer)

    class OrderTable(Base):
        __tablename__ = "orders"
        id = column(Integer, primary_key=True, index =True)
        product_id = column(Integer, foreign_key("products.id"))
        quantity = column(Integer)
        total_price = column(float)
        status = column(String)
        order_date = column(String)

        Base.metadata.create_all(bind=engine)
        app = FastAPI(title="Order Management API")
def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()
        