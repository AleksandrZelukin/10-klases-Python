import tkinter as tk

a = tk.Tk()

a.geometry("600x300+800+300")
a.title("Riņka laukuma noteikšana")


logs1 = tk.Entry(a, width=5, font=("size 32"))
logs1.place(x=100, y=10)

s = tk.Label(text = "X", font=("size 32"))
s.place(x=250, y=10)

#logs2 = tk.Entry(a, width=5, font=("size 32"))
#logs2.place(x=300, y=10)
pi = tk.Label(text = "3,14...", font=("size 32"))
pi.place(x=300, y=10)

label = tk.Label(text = "Sveiki, draugs!", font=("size 32"))
label.place(x=150, y=70)

def clear():
    label.config(text="Sveiki, draugs!")

def reizinajums():
    one = float(logs1.get())
    two = 3.14
    result = one * two
    label.configure(text = "= %s" % result)

def ievads():
    label["text"] = logs1.get()

btn1 = tk.Button(a, text="ievads", command=reizinajums)
btn1.place(x=200, y=120)

btn2 = tk.Button(a, text="notirit", command=clear)
btn2.place(x=270, y=120)

a.mainloop()