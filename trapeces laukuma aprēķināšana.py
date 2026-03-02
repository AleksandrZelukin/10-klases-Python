#from tkinter import *
import tkinter as tk
from tkinter import Label, Entry, Button, PhotoImage, Tk
win = tk.Tk()
win.title("trapeces laukums")
win.geometry("320x380")

nos = Label(text="trapeces laukuma aprēķināšana")
nos.pack()
lbl_a=Label(text="a mala")
lbl_a.pack()
a = Entry(width=8)
a.pack()
lbl_b=Label(text="b mala")
lbl_b.pack()
b = Entry(width=8)
b.pack()
lbl_h=Label(text="h augstums")
lbl_h.pack()
h = Entry(width=8)
h.pack()
rezultats = Label()
rezultats.pack()

def s():
  pirmais = float(a.get())
  otrais = float(b.get())
  tresais = float(h.get())
  rez = (pirmais+otrais)*tresais/2
  rezultats.configure(text = rez)


btn1 = Button(text="parādīt aprēķina rezultātu",command=s)
btn1.pack()

# trap = PhotoImage(file='trapecija.gif')
# izo = Label(image=trap)
# izo.pack()
win.mainloop()
