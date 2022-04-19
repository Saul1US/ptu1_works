from sqlalchemy import Column, Integer, String, ForeignKey, Float, create_engine, DateTime, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime, date

engine = create_engine('sqlite:///stock.db')
Base = declarative_base()

class Unit(Base):
    __tablename__ = "unit"
    id = Column(Integer, primary_key=True, autoincrement=True)
    unit_name = Column("Unit Name", String)

    def __repr__(self):
        return f"{self.id}: {self.unit_name}"

class Product(Base):
    __tablename__ = "product"
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_name = Column("Product Name", String)
    min_qty = Column("Minumum Quantity", Float)
    unit_id = Column(Integer, ForeignKey("unit.id"))
    unit = relationship("Unit")

    def __repr__(self):
        return f"{self.id}: {self.product_name}, {self.min_qty}, {self.unit}"

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_date = Column("Order Date", Date)
    product_id = Column(Integer, ForeignKey("product.id"))
    product = relationship("Product")
    unit_id = Column(Integer, ForeignKey("unit.id"))
    unit = relationship("Unit")
    expiry_date = Column("Expiry Date", Date)
    
    def __repr__(self):
        return f"{self.id}: {self.order_date}, {self.product}, {self.unit}, {self.expiry_date}"

class Stock(Base):
    __tablename__ = "stock"
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    order = relationship("Order")
    product_id = Column(Integer, ForeignKey("product.id"))
    product = relationship("Product")
    stock_qty = Column("Stock Quantity", Float)
    unit_id = Column(Integer, ForeignKey("unit.id"))
    unit = relationship("Unit")

    def __repr__(self):
        return f"{self.id}: {self.order}, {self.product}, {self.unit}"


class ShoppingList(Base):
    __tablename__ = "shopping_list"
    id = Column(Integer, primary_key=True, autoincrement=True)
    stock_id = Column(Integer, ForeignKey("stock.id"))
    stock = relationship("Stock")

    def __repr__(self):
        return f"{self.stock}"

class Expiry(Base):
    __tablename__ = "expiry"
    id = Column(Integer, primary_key=True, autoincrement=True)
    stock_id = Column(Integer, ForeignKey("stock.id"))
    stock = relationship("Stock")

    def __repr__(self):
        return f"{self.stock}"



Base.metadata.create_all(engine)