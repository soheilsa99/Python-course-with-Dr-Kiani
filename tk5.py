class product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def show(self):
        return self.id, self.name, self.price


from tkinter import messagebox
from tkinter import *
master = Tk()
Label(master, text='ID: ').grid(row=0)
Label(master, text='name: ').grid(row=1)
Label(master, text='Price ').grid(row=2)
Label(master, text="Price: ").grid(row=2)
ent_id_product = Entry(master)
ent_name_product = Entry(master)
ent_price_product = Entry(master)
Label(master, text="Price: ").grid(row=2)
ent_id_product.grid(row=0, column=1)
ent_name_product.grid(row=1, column=1)
ent_price_product.grid(row=2, column=1)
L = []
lb = Listbox(master)
lb.grid(row=4, column=1)

def add():
    p = product(ent_id_product.get(), ent_name_product.get(), int(ent_price_product.get()))
    L.append(p)
    messagebox.showinfo('Alert', ent_name_product.get()+' was appended to list')

def show():
    for p in L:
        lb.insert(END, p.show())


btn1 = Button(master, text='add', width=25, command=add)
btn2 = Button(master, text='show', width=25, command=show)
btn1.grid(row=3, column=1)
btn2.grid(row=3, column=0)

mainloop()
