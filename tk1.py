import tkinter
m = tkinter.Tk()

m.mainloop()
# we uae mainloop() for keep open the menu


# ----------------------------------------------------------
import tkinter as tk
r = tk.Tk()
r.title('Counting Second')

button = tk.Button(r, text='Stop', width=25, command=r.destroy)
button.pack()
r.mainloop()


# ----------------------------------------------------------
import tkinter as tk
r = tk.Tk()
r.title('Counting Second')
def fun():
    print('hello')

button = tk.Button(r, text='Stop', width=25, command=fun)
button.pack()
r.mainloop()


