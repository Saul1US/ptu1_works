from sqlalchemy import Column, Integer, String, ForeignKey, Float, create_engine, DateTime, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime, date

engine = create_engine('sqlite:///stock.db')
Base = declarative_base()

class Unit(Base):
    __tablename__ = "unit"
    id = Column(Integer, primary_key=True)
    unit_name = Column("unit_name", String)

    def __init__ (self, unit_name):
        self.unit_name = unit_name

    def __repr__(self):
        return f"{self.id}: {self.unit_name}"

class Product(Base):
    __tablename__ = "product"
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_name = Column("product_name", String)
    min_qty = Column("minumum_quantity", Float)
    unit_id = Column(Integer, ForeignKey("unit.id"))
    unit = relationship("Unit")

    def __init__ (self, product_name, min_qty, unit_id):
        self.product_name = product_name
        self.min_qty = min_qty
        self.unit_id = unit_id

    def __repr__(self):
        return f"{self.id}: {self.product_name}"

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_date = Column("order_date", Date)
    product_id = Column(Integer, ForeignKey("product.id"))
    product = relationship("Product")
    quantity = Column("quantity", Float)
    unit_id = Column(Integer, ForeignKey("unit.id"))
    unit = relationship("Unit")
    expiry_date = Column("expiry_date", Date)

    def __init__ (self, order_date, product_id, quantity, unit_id, expiry_date):
        self.order_date = order_date
        self.product_id = product_id
        self.quantity = quantity
        self.unit_id = unit_id
        self.expiry_date = expiry_date
    
    def __repr__(self):
        return f"{self.id}: {self.order_date}, {self.product}, {self.quantity}, {self.unit}, {self.expiry_date}"

class Stock(Base):
    __tablename__ = "stock"
    id = Column(Integer, primary_key=True, autoincrement=True)
    # order_id = Column(Integer, ForeignKey("orders.id"))
    # order = relationship("Order")
    product_id = Column(Integer, ForeignKey("product.id"))
    product = relationship("Product")
    stock_qty = Column("stock_qty", Float)
    unit_id = Column(Integer, ForeignKey("unit.id"))
    unit = relationship("Unit")

    def __init__ (self, product_id, stock_qty, unit_id):
        self.product_id = product_id
        self.stock_qty = stock_qty
        self.unit_id = unit_id

    def __repr__(self):
        return f"{self.product}, {self.stock_qty}, {self.unit}"


class ShoppingList(Base):
    __tablename__ = "shopping_list"
    id = Column(Integer, primary_key=True, autoincrement=True)
    stock_id = Column(Integer, ForeignKey("stock.id"))
    stock = relationship("Stock")
    
    def __init__ (self, stock_id):
        self.stock_id = stock_id

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