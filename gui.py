from dbcon import *
from tkinter import *
from datetime import datetime

class WindowMain:
    def __init__(self, master):
        self.master = master
        self.button1 = Button(self.master, width=40, text="Enter Units", command=self.new_window1)
        self.button2 = Button(self.master, width=40, text="Enter Products", command=self.new_window2)
        self.button3 = Button(self.master, width=40, text="Enter Orders", command=self.new_window3)
        self.button4 = Button(self.master, width=40, text="Take Stock", command=self.new_window4)
        self.button1.grid(row=1, column=1)
        self.button2.grid(row=2, column=1)
        self.button3.grid(row=3, column=1)
        self.button4.grid(row=4, column=1)

        meniu1 = Menu(self.master)
        self.master.config(menu=meniu1)
        submeniu = Menu(meniu1, tearoff=False)
        meniu1.add_cascade(label="Lists", menu=submeniu)
        submeniu.add_command(label="Unit List", command=self.unit_list_window)
        submeniu.add_command(label="Product List", command=self.product_list_window)
        submeniu.add_command(label="Order List", command=self.order_list_window)
        submeniu.add_command(label="Stock List", command=self.stock_list_window)
        submeniu.add_command(label="Shopping List", command=self.shopping_list_window)

    def new_window1(self):
        self.newWindow = Toplevel(self.master)
        self.app = WindowUnit(self.newWindow)

    def new_window2(self):
        self.newWindow = Toplevel(self.master)
        self.app = WindowProduct(self.newWindow)

    def new_window3(self):
        self.newWindow = Toplevel(self.master)
        self.app = WindowOrder(self.newWindow)

    def new_window4(self):
        self.newWindow = Toplevel(self.master)
        self.app = WindowStock(self.newWindow)

    def unit_list_window(self):
        self.unit_window = Toplevel(self.master)
        self.unit_window.geometry("300x200")
        self.scrollbar1 = Scrollbar(self.unit_window)
        self.listbox1 = Listbox(self.unit_window, width=30, yscrollcommand=self.scrollbar1.set)
        self.scrollbar1.config(command=self.listbox1.yview)
        self.list1 = get_unit_list()
        self.listbox1.insert(END, *self.list1)
        self.listbox1.pack(side=LEFT)
        self.scrollbar1.pack(side=RIGHT, fill=Y)

    def product_list_window(self):
        self.product_window = Toplevel(self.master)
        self.product_window.geometry("300x200")
        self.scrollbar1 = Scrollbar(self.product_window)
        self.listbox1 = Listbox(self.product_window, width=30, yscrollcommand=self.scrollbar1.set)
        self.scrollbar1.config(command=self.listbox1.yview)
        self.list1 = get_product_list()
        self.listbox1.insert(END, *self.list1)
        self.listbox1.pack(side=LEFT)
        self.scrollbar1.pack(side=RIGHT, fill=Y)

    def order_list_window(self):
        self.order_window = Toplevel(self.master)
        self.order_window.geometry("400x300")
        self.scrollbar1 = Scrollbar(self.order_window)
        self.listbox1 = Listbox(self.order_window, width=50, yscrollcommand=self.scrollbar1.set)
        self.scrollbar1.config(command=self.listbox1.yview)
        self.list1 = get_order_list()
        self.listbox1.insert(END, *self.list1)
        self.listbox1.pack(side=LEFT)
        self.scrollbar1.pack(side=RIGHT, fill=Y)

    def stock_list_window(self):
        self.stock_window = Toplevel(self.master)
        self.stock_window.geometry("400x300")
        self.scrollbar1 = Scrollbar(self.stock_window)
        self.listbox1 = Listbox(self.stock_window, width=50, yscrollcommand=self.scrollbar1.set)
        self.scrollbar1.config(command=self.listbox1.yview)
        self.list1 = get_stock_list()
        self.listbox1.insert(END, *self.list1)
        self.listbox1.pack(side=LEFT)
        self.scrollbar1.pack(side=RIGHT, fill=Y)

    def shopping_list_window(self):
        self.shop_list_window = Toplevel(self.master)
        self.shop_list_window.geometry("400x300")
        self.scrollbar1 = Scrollbar(self.shop_list_window)
        self.listbox1 = Listbox(self.shop_list_window, width=50, yscrollcommand=self.scrollbar1.set)
        self.scrollbar1.config(command=self.listbox1.yview)
        self.list1 = get_shopping_list()
        self.listbox1.insert(END, *self.list1)
        self.listbox1.pack(side=LEFT)
        self.scrollbar1.pack(side=RIGHT, fill=Y)

class WindowUnit:
    def __init__(self, master):
        self.master = master
        self.unit_name = Label(self.master, text="Unit Name")
        self.entry_field = Entry(self.master)
        self.enter_button = Button(self.master, text = 'Enter')
        self.enter_button.bind("<Button-1>", lambda event: add_unit(self.entry_field.get()))
        self.unit_name.grid(row=0, column=0, sticky=E)
        self.entry_field.grid(row=0, column=1)
        self.enter_button.grid(row=1, column=1)

class WindowProduct:
    def __init__(self, master):
        self.master = master
        self.product_name = Label(self.master, text="Product Name")
        self.min_qty = Label(self.master, text="Minimum Quantity")
        self.unit = Label(self.master, text="Unit")
        self.prod_entry_field = Entry(self.master)
        self.qty_entry_field = Entry(self.master)
        self.enter_button = Button(self.master, text = 'Enter')
        self.enter_button.bind("<Button-1>", lambda event: add_product(self.prod_entry_field.get(), self.qty_entry_field.get(), self.choice.get()))
        self.unit_drop = get_unit_list()
        self.choice = StringVar()
        self.choice.set("select unit")
        self.drop = OptionMenu(self.master, self.choice, *self.unit_drop)
        self.drop.grid(row=2, column=1)
        self.unit.grid(row=2, column=0)
        self.product_name.grid(row=0, column=0, sticky=E)
        self.min_qty.grid(row=1, column=0, sticky=E)
        self.prod_entry_field.grid(row=0, column=1)
        self.qty_entry_field.grid(row=1, column=1)
        self.enter_button.grid(row=3, column=1)
    

class WindowOrder:
    def __init__(self, master):
        self.master = master
        self.order_date = Label(self.master, text="Order Date YYYY-MM-DD")
        self.product = Label(self.master, text="Product")
        self.quantity = Label(self.master, text="Quantity")
        self.unit = Label(self.master, text="Unit")
        self.expiry_date = Label(self.master, text="Expiry Date YYYY-MM-DD")
        self.order_date_field = Entry(self.master)
        self.quantity_field = Entry(self.master)
        self.expiry_date_field = Entry(self.master)
        self.enter_button1 = Button(self.master, width=20, text = 'Enter Order')
        self.enter_button2 = Button(self.master, width=20, text = 'Enter Stock')
        self.enter_button1.bind("<Button-1>", lambda event: add_order(datetime.strptime(self.order_date_field.get(), "%Y-%m-%d"), self.choice_product.get(), self.quantity_field.get(), self.choice_unit.get(), datetime.strptime(self.expiry_date_field.get(), "%Y-%m-%d")))
        self.enter_button2.bind("<Button-1>", lambda event: add_stock(self.choice_product.get(), self.quantity_field.get(), self.choice_unit.get()))
        self.product_drop = get_product_list()
        self.choice_product = StringVar()
        self.choice_product.set("select product")
        self.drop1 = OptionMenu(self.master, self.choice_product, *self.product_drop)
        self.drop1.grid(row=1, column=1)
        self.unit_drop = get_unit_list()
        self.choice_unit = StringVar()
        self.choice_unit.set("select unit")
        self.drop2 = OptionMenu(self.master, self.choice_unit, *self.unit_drop)
        self.drop2.grid(row=3, column=1)
        self.order_date.grid(row=0, column=0)
        self.product.grid(row=1, column=0)
        self.quantity.grid(row=2, column=0)
        self.unit.grid(row=3, column=0)
        self.expiry_date.grid(row=4, column=0)
        self.order_date_field.grid(row=0, column=1)
        self.quantity_field.grid(row=2, column=1)
        self.expiry_date_field.grid(row=4, column=1)
        self.enter_button1.grid(row=5, column=1)
        self.enter_button2.grid(row=6, column=1)
        

class WindowStock:
    def __init__(self, master):
        self.master = master
        self.product = Label(self.master, text="Product")
        self.unit = Label(self.master, text="Unit")
        self.product_drop = get_product_list()
        self.choice_product = StringVar()
        self.choice_product.set("select product")
        self.drop1 = OptionMenu(self.master, self.choice_product, *self.product_drop)
        self.drop1.grid(row=0, column=1)
        self.stock_qty = Label(self.master, text="Used Quantity")
        self.qty_field = Entry(self.master)
        self.unit_drop = get_unit_list()
        self.choice_unit = StringVar()
        self.choice_unit.set("select unit")
        self.drop2 = OptionMenu(self.master, self.choice_unit, *self.unit_drop)
        self.drop2.grid(row=2, column=1)
        self.enter_button1 = Button(self.master, text = 'Enter')
        self.enter_button1.bind("<Button-1>", lambda event: self.stock_op(self.choice_product.get(), self.qty_field.get()))
        self.product.grid(row=0, column=0, sticky=E)
        self.stock_qty.grid(row=1, column=0, sticky=E)
        self.unit.grid(row=2, column=0)
        self.qty_field.grid(row=1, column=1)
        self.enter_button1.grid(row=3, column=1)
        
    def stock_op(self, selected_prod_id, used_qty):
        self.selected_prod_id = selected_prod_id
        self.used_qty = float(used_qty)
        self.selected_id = self.selected_prod_id[0]
        self.req_qty = session.query(Stock.stock_qty).where(Stock.product_id == self.selected_id).scalar()
        self.left_qty = self.req_qty - self.used_qty
        self.req_id = session.query(Stock.id).where(Stock.product_id == self.selected_id).scalar()
        update_stock(self.req_id, self.left_qty)
        self.min_qty = session.query(Product.min_qty).where(Product.id == self.selected_id).scalar()
        if self.left_qty < self.min_qty:
            update_shoping_list(self.req_id)
            
        
def main():
    root = Tk()
    root.geometry("300x200")
    app = WindowMain(root)
    root.mainloop()

if __name__ == '__main__':
    main()