import math
import tkinter as tk
from tkinter import *
from tkinter import ttk

window = tk.Tk()

window.geometry('150x200')
lbl1 = Label(window, fg='#f00', text="W=", font=("Arial Bold", 10))
lbl1.grid(column=0, row=0) 
lbl2 = Label(window, fg='#f00', text="C=", font=("Arial Bold", 10))
lbl2.grid(column=0, row=1)  
lbl3 = Label(window, fg='#f00', text="U=", font=("Arial Bold", 10))
lbl3.grid(column=0, row=2)  
  

w = tk.IntVar()
nameEntered1 = ttk.Entry(window, width = 15, foreground='#f00', textvariable = w)
nameEntered1.grid(column = 1, row = 0)
c = tk.IntVar()
nameEntered2 = ttk.Entry(window, width = 15, foreground='#f00', textvariable = c)
nameEntered2.grid(column = 1, row = 1)
u = tk.IntVar()
nameEntered3 = ttk.Entry(window, width = 15, foreground='#f00', textvariable = u)
nameEntered3.grid(column = 1, row = 2)


def Rabotai():
        d  = u.get() * u.get() 
        d1 = c.get()* d
        d2 = d1/2
        nameEntered1.delete(0,"")
        nameEntered1.insert(0,d2)

b1 = Button(text="Вычислить", width=13, height=3, foreground='#f00', command=Rabotai)
b1.grid(column=1, row=3)



window.mainloop()
