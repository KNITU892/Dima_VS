import tkinter as tk
from tkinter import *
from tkinter import ttk

window = tk.Tk()

window.geometry('150x200')
lbl1 = Label(window, fg='#f00', text="Q=", font=("Arial Bold", 10))
lbl1.grid(column=0, row=0) 
lbl2 = Label(window, fg='#f00', text="c=", font=("Arial Bold", 10))
lbl2.grid(column=0, row=1)  
lbl3 = Label(window, fg='#f00', text="t1=", font=("Arial Bold", 10))
lbl3.grid(column=0, row=2)  
lbl4 = Label(window, fg='#f00', text="t2=", font=("Arial Bold", 10))
lbl4.grid(column=0, row=3)  
lbl5 = Label(window, fg='#f00', text="m=", font=("Arial Bold", 10)) 
lbl5.grid(column=0,row=4)  

q = tk.IntVar()
nameEntered1 = ttk.Entry(window, width = 15, foreground='#f00', textvariable = q)
nameEntered1.grid(column = 1, row = 0)
c = tk.IntVar()
nameEntered2 = ttk.Entry(window, width = 15, foreground='#f00', textvariable = c)
nameEntered2.grid(column = 1, row = 1)
t1 = tk.IntVar()
nameEntered3 = ttk.Entry(window, width = 15, foreground='#f00', textvariable = t1)
nameEntered3.grid(column = 1, row = 2)
t2 = tk.IntVar()
nameEntered4 = ttk.Entry(window, width = 15, foreground='#f00', textvariable = t2)
nameEntered4.grid(column = 1, row = 3)
m = tk.IntVar()
nameEntered5 = ttk.Entry(window, width = 15, foreground='#f00', textvariable = m)
nameEntered5.grid(column = 1, row = 4)

def Rabotai():
	d = t2.get()-t1.get()
	d1 = c.get()*m.get()
	d2 = d1*d
	nameEntered1.delete(0,"")
	nameEntered1.insert(0,d2) 

b1 = Button(text="Вычислить", width=13, height=3, foreground='#f00', command=Rabotai)
b1.grid(column=1, row=5)



window.mainloop()