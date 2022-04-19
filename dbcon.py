from models.stocks import Unit, Product, Order, Stock, ShoppingList, Expiry
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///stock.db')
Session = sessionmaker(bind=engine)
session = Session()

def add_unit(unit_name):
    unit = Unit(unit_name)
    session.add(unit)
    session.commit()

def add_product(product_name, min_qty):
    product = Product(product_name, min_qty)
    session.add(product)
    session.commit()

def add_order(order_date, expiry_date):
    order = Order(order_date, expiry_date)
    session.add(order)
    session.commit()

def get_product_list():
    return session.query(Product).all()

def get_order_list():
    return session.query(Order).all()

def get_stock_list():
    return session.query(Stock).all()

def get_shopping_list():
    return session.query(ShoppingList).all()

def get_expiry_list():
    return session.query(Expiry).all()

