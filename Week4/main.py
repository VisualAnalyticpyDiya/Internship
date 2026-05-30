from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel
from typing import List
import datetime

DATABASE_URL = "sqlite:///./orders.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class ProductTable(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float)
    stock = Column(Integer)

class OrderTable(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer)
    total_price = Column(Float)
    status = Column(String)
    order_date = Column(String, default=str(datetime.datetime.now()))

Base.metadata.create_all(bind=engine)
app = FastAPI(title="Order Management API")

def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()

class OrderCreate(BaseModel):
    product_id: int
    quantity: int

@app.on_event("startup")
def setup_dummy_products():
    db = SessionLocal()
    if db.query(ProductTable).count() == 0:
        p1 = ProductTable(name="Laptop", price=1000.0, stock=10)
        p2 = ProductTable(name="Smartphone", price=500.0, stock=30)
        db.add_all([p1, p2])
        db.commit()
    db.close()

@app.get("/products")
def get_products(db: Session = Depends(get_db)):
    return db.query(ProductTable).all() 

@app.post("/orders")
def create_order(order_data: OrderCreate, db: Session = Depends(get_db)):
    product = db.query(ProductTable).filter(ProductTable.id == order_data.product_id).first()
    
    if not product:
        raise HTTPException(status_code=404, detail="product not found")
        
    if product.stock < order_data.quantity:
        rejected_order = OrderTable(
            product_id=order_data.product_id,
            quantity=order_data.quantity,
            total_price=0.0,
            status="rejected"
        )   
        db.add(rejected_order)   
        db.commit()
        raise HTTPException(status_code=400, detail="insufficient stock")
        
    calculate_total = product.price * order_data.quantity
    product.stock = product.stock - order_data.quantity
    
    new_order = OrderTable(
        product_id=order_data.product_id,
        quantity=order_data.quantity,
        total_price=calculate_total,
        status="Success"
    )
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return {"message": "Order placed successfully!", "order_details": new_order}

@app.get("/orders")
def get_order_history(db: Session = Depends(get_db)):
    return db.query(OrderTable).all()