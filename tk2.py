import tkinter as tk
r = tk.Tk()
r.title('Counting Second')
from tkinter import messagebox
def fun():
    # print('hello')
    messagebox.showinfo('alert', 'hello')

button = tk.Button(r, text='Stop', width=25, command=fun())
button.pack()
r.mainloop()

#----------------------------------------------------------------
import tkinter as tk
r = tk.Tk()
r.title('Counting Second')
from tkinter import messagebox
def fun():
    # print('hello')
    messagebox.showwarning('alert', 'hello')

button = tk.Button(r, text='Stop', width=25, command=fun())
button.pack()
r.mainloop()

#----------------------------------------------------------
import tkinter as tk
r = tk.Tk()
r.title('Counting Second')
from tkinter import messagebox
def fun():
    # print('hello')
    messagebox.showinfo('alert', 'hello')

button = tk.Button(r, text='Stop', width=25, command=fun())
button.pack()
r.mainloop()