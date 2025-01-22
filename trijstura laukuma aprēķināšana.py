from tkinter import *

win = Tk()
win.title("trijstura laukums")
win.geometry("320x380")

nos = Label(text="trijstura laukuma aprēķināšana")
nos.pack()
lbl_a=Label(text="a katets")
lbl_a.pack()
a = Entry(width=8)
a.pack()
lbl_b=Label(text="b katets")
lbl_b.pack()
b = Entry(width=8)
b.pack()
rezultats = Label()
rezultats.pack()

def s():
  pirmais = float(a.get())
  otrais = float(b.get())
  
  rez = (pirmais*otrais)/2
  rezultats.configure(text = rez)
  f = open("trijstura_laukuma_aprekinosana.txt","a")
  print(f"Trijstura ar katetam {pirmais} un {otrais} laukums ir {rez}", file=f)
  f.close()

btn1 = Button(text="parādīt aprēķina rezultātu",command=s)
btn1.pack()

trap = PhotoImage(file='trijsturis.gif')
izo = Label(image=trap)
izo.pack()
win.mainloop()
