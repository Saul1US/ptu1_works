from dbcon import *
from tkinter import *
from datetime import datetime

class WindowMain:
    def __init__(self, master):
        self.master = master
        self.button1 = Button(self.master, width=40, text="Enter Units", command=self.new_window1)
        self.button2 = Button(self.master, width=40, text="Enter Products", command=self.new_window2)
        self.button3 = Button(self.master, width=40, text="Enter Orders", command=self.new_window3)
        self.button1.grid(row=1, column=1)
        self.button2.grid(row=2, column=1)
        self.button3.grid(row=3, column=1)

    def new_window1(self):
        self.newWindow = Toplevel(self.master)
        self.app = WindowUnit(self.newWindow)

    def new_window2(self):
        self.newWindow = Toplevel(self.master)
        self.app = WindowProduct(self.newWindow)

    def new_window3(self):
        self.newWindow = Toplevel(self.master)
        self.app = WindowOrder(self.newWindow)

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
        self.order_date = Label(self.master, text="Order Date")
        self.product = Label(self.master, text="Product")
        self.unit = Label(self.master, text="Unit")
        self.expiry_date = Label(self.master, text="Expiry Date YY-MM-DD")
        self.order_date_field = Entry(self.master)
        self.expiry_date_field = Entry(self.master)
        self.enter_button1 = Button(self.master, text = 'Enter')
        self.enter_button1.bind("<Button-1>", lambda event: add_order(datetime.strptime(self.order_date_field.get(), "%Y-%m-%d"), self.choice_product.get(), self.choice_unit.get(), datetime.strptime(self.expiry_date_field.get(), "%Y-%m-%d")))
        self.product_drop = get_product_list()
        self.choice_product = StringVar()
        self.choice_product.set("select product")
        self.drop = OptionMenu(self.master, self.choice_product, *self.product_drop)
        self.drop.grid(row=1, column=1)
        self.unit_drop = get_unit_list()
        self.choice_unit = StringVar()
        self.choice_unit.set("select unit")
        self.drop = OptionMenu(self.master, self.choice_unit, *self.unit_drop)
        self.drop.grid(row=2, column=1)
        self.order_date.grid(row=0, column=0)
        self.product.grid(row=1, column=0)
        self.unit.grid(row=2, column=0)
        self.expiry_date.grid(row=3, column=0)
        self.order_date_field.grid(row=0, column=1)
        self.expiry_date_field.grid(row=3, column=1)
        self.enter_button1.grid(row=4, column=1)


    # def get_unit(self):
    #     self.a = "kg"
    #     return self.a
        # unit_list = get_unit_list()
        # for i in args:
        # print(unit_list)
    # get_unit()
            


    def close_windows(self):
        self.master.destroy()

def main():
    root = Tk()
    root.geometry("300x200")
    app = WindowMain(root)
    root.mainloop()

if __name__ == '__main__':
    main()