from models.stocks import Unit, Product, Order, Stock
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///stock.db')
Session = sessionmaker(bind=engine)
session = Session()

def add_unit(unit_name):
    unit = Unit(unit_name)
    session.add(unit)
    session.commit()

def add_product(product_name, min_qty, unit_id):
    product = Product(product_name, min_qty, unit_id[0])
    session.add(product)
    session.commit()

def add_order(order_date, product_id, quantity, unit_id, expiry_date):
    order = Order(order_date, product_id[0], quantity, unit_id[0], expiry_date)
    # stock = Stock(order_id, product_id[0], quantity, unit_id[0])
    session.add(order)
    # session.add(stock)
    session.commit()

def add_stock(product_id, stock_qty, unit_id):
    stock = Stock(product_id[0], stock_qty, unit_id[0])
    session.add(stock)
    session.commit()

# def add_stock(order_id, product_id, stock_qty, unit_id):
#     stock = Stock(order_id, product_id, stock_qty, unit_id)
#     session.add(stock)
#     session.commit()

def get_unit_list():
    print(session.query(Unit).all())
    return session.query(Unit).all()

def get_product_list():
    print(session.query(Product).all())
    return session.query(Product).all()

def get_order_list():
    return session.query(Order).all()

def get_stock_list():
    return session.query(Stock).all()

# def get_shopping_list():
#     return session.query(ShoppingList).all()

# def get_expiry_list():
#     return session.query(Expiry).all()

# print(get_product_list())