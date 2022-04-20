from models.stocks import Unit, Product, Order, Stock
from sqlalchemy import create_engine, select, MetaData, Table, and_
from sqlalchemy.orm import sessionmaker
# import sqlalchemy as db

engine = create_engine('sqlite:///stock.db')
Session = sessionmaker(bind=engine)
session = Session()

# metadata = MetaData()
# stock9 = Table('stock', metadata, autoload=True, autoload_with=engine)

# def get_stock_qty():
# stock1 = select(Stock.stock_qty).where(Stock.product_id == "2")
# connection = engine.connect()
# results = connection.execute(stock1).fetchall()
# print(results)
# get_stock_qty()

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
    stock = Stock(product_id[0], stock_qty, unit_id[0])
    session.add(stock)
    session.commit()

def update_stock(id1, newstock_qty):
    print(id1, newstock_qty)
    stock = session.query(Stock).get(id1)
    # stock.product_id = newproduct_id
    stock.stock_qty = newstock_qty
    # stock.unit_id = newunit_id
    session.commit()
    # session.update(stock).where(Stock.product_id == 2).values(stock_qty = 8)
# update_stock(2, 7)

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
    # duomenys = session.query(Stock.stock_qty).where(Stock.product_id == 2).scalar()
    # print(duomenys)
    return session.query(Stock).all()

# def get_stock_qty():
#     req_qty = session.query(Stock.stock_qty).where(Stock.product_id == 2).scalar()
#     return req_qty

# def get_shopping_list():
#     return session.query(ShoppingList).all()

# def get_expiry_list():
#     return session.query(Expiry).all()

# print(get_product_list())