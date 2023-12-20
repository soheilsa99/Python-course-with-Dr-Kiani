from tkinter import *

master = Tk()
Label(master, text='First Name').grid(row=0)
Label(master, text='Last Name').grid(row=1)
e1 = Entry(master)
e2 = Entry(master)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
def fun():
    print(e1.get()+' '+e2.get())
button = Button(master, text='show', width=25, command=fun)
button.grid(row=2, column=1)
mainloop()

#---------------------------------------------------
from tkinter import *
from tkinter import messagebox

master = Tk()
Label(master, text='First Name').grid(row=0)
Label(master, text='Last Name').grid(row=1)
e1 = Entry(master)
e2 = Entry(master)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
def fun():
    # print(e1.get()+' '+e2.get())
    messagebox.showinfo('alert', e1.get()+' '+e2.get())
button = Button(master, text='show', width=25, command=fun)
button.grid(row=2, column=1)
mainloop()
