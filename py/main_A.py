import math
import tkinter as tk
from tkinter import *
from tkinter import ttk

window = tk.Tk()

window.geometry('150x200')
lbl1 = Label(window, fg='#f00', text="A=", font=("Arial Bold", 10))
lbl1.grid(column=0, row=0) 
lbl2 = Label(window, fg='#f00', text="m=", font=("Arial Bold", 10))
lbl2.grid(column=0, row=1)  
lbl3 = Label(window, fg='#f00', text="M=", font=("Arial Bold", 10))
lbl3.grid(column=0, row=2)
lbl4 = Label(window, fg='#f00', text="t1=", font=("Arial Bold", 10))
lbl4.grid(column=0, row=3)  
lbl5 = Label(window, fg='#f00', text="t2=", font=("Arial Bold", 10))
lbl5.grid(column=0, row=4)
lbl6 = Label(window, fg='#f00', text="R=", font=("Arial Bold", 10))
lbl6.grid(column=0, row=5)
  
  

i = tk.IntVar()
nameEntered1 = ttk.Entry(window, width = 15, foreground='#f00', textvariable = i)
nameEntered1.grid(column = 1, row = 0)
m = tk.IntVar()
nameEntered2 = ttk.Entry(window, width = 15, foreground='#f00', textvariable = m)
nameEntered2.grid(column = 1, row = 1)
M = tk.IntVar()
nameEntered3 = ttk.Entry(window, width = 15, foreground='#f00', textvariable = M)
nameEntered3.grid(column = 1, row = 2)
t1 = tk.IntVar()
nameEntered4 = ttk.Entry(window, width = 15, foreground='#f00', textvariable = t1)
nameEntered4.grid(column = 1, row = 3)
t2 = tk.IntVar()
nameEntered5 = ttk.Entry(window, width = 15, foreground='#f00', textvariable = t2)
nameEntered5.grid(column = 1, row = 4)
R = tk.IntVar()
nameEntered6 = ttk.Entry(window, width = 15, foreground='#f00', textvariable = R)
nameEntered6.grid(column = 1, row = 5)

def Rabotai():
	d = m.get()/M.get()
	d1 = t1.get()*t2.get()
	d2 = (-(3/2)*d)/d1
	nameEntered1.delete(0,"")
	nameEntered1.insert(0,d2) 

b1 = Button(text="Вычислить", width=13, height=3, foreground='#f00', command=Rabotai)
b1.grid(column=1, row=6)



window.mainloop()
