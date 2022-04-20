from models.stocks import Unit, Product, Order, Stock
from sqlalchemy import create_engine, select, MetaData, Table, and_
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
    session.add(order)
    session.commit()

def add_stock(product_id, stock_qty, unit_id):
    selected_prod = product_id[0]
    req_id = session.query(Stock.id).where(Stock.product_id == selected_prod).scalar()
    req_qty = session.query(Stock.stock_qty).where(Stock.product_id == selected_prod).scalar()
    stock = session.query(Stock).get(req_id)
    if stock != None:
        newstock_qty = float(stock_qty) + float(req_qty)
        update_stock(req_id, newstock_qty)
    else:
        stock = Stock(product_id[0], stock_qty, unit_id[0])
        session.add(stock)
        session.commit()

def update_stock(selected_id, newstock_qty):
    stock = session.query(Stock).get(selected_id)
    stock.stock_qty = newstock_qty
    session.commit()

def get_unit_list():
    return session.query(Unit).all()

def get_product_list():
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