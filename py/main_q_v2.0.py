import tkinter as tk
from tkinter import *
from tkinter import ttk

window = tk.Tk()

window.geometry('150x200')
lbl1 = Label(window, fg='#f00', text="Q=", font=("Arial Bold", 10))
lbl1.grid(column=0, row=0) 
lbl2 = Label(window, fg='#f00', text="m=", font=("Arial Bold", 10))
lbl2.grid(column=0, row=1)  
lbl3 = Label(window, fg='#f00', text="r=", font=("Arial Bold", 10))
lbl3.grid(column=0, row=2)  


q = tk.IntVar()
nameEntered1 = ttk.Entry(window, width = 15, foreground='#f00', textvariable = q)
nameEntered1.grid(column = 1, row = 0)
m = tk.IntVar()
nameEntered2 = ttk.Entry(window, width = 15, foreground='#f00', textvariable = m)
nameEntered2.grid(column = 1, row = 1)
r = tk.IntVar()
nameEntered3 = ttk.Entry(window, width = 15, foreground='#f00', textvariable = r)
nameEntered3.grid(column = 1, row = 2)


def Rabotai():
	d1 = r.get()*m.get()
	nameEntered1.delete(0,"")
	nameEntered1.insert(0,d1) 

b1 = Button(text="Вычислить", width=13, height=3, foreground='#f00', command=Rabotai)
b1.grid(column=1, row=5)



window.mainloop()
