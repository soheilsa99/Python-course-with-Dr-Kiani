# sum 2 number
from tkinter import *
from tkinter import messagebox

master = Tk()
Label(master, text='first number').grid(row=0)
Label(master, text='second number').grid(row=1)
e1 = Entry(master)
e2 = Entry(master)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
def fun():
    messagebox.showinfo('alert', int(e1.get())+int(e2.get()))
button = Button(master, text='sum', width=25, command=fun)
button.grid(row=2, column=1)
mainloop()