import tkinter as tk

a = tk.Tk()

a.geometry("600x300+800+300")
a.title("Taisnstura laukuma noteiksana")


logs1 = tk.Entry(a, width=5, font=("size 32"))
logs1.grid(row=1, column=1)

logs2 = tk.Entry(a, width=5, font=("size 32"))
logs2.grid(row=1, column=3)

s = tk.Label(text = "X", font=("size 32"))
s.grid(row=1, column=2)
label = tk.Label(text = "Sveiki, draugs!", font=("size 32"))
label.grid(row=2, column=1, columnspan=2)

def clear():
    label.config(text="Sveiki, draugs!")

def reizinajums():
    one = float(logs1.get())
    two = float(logs2.get())
    result = one * two
    label.configure(text = "= %s" % result)

def ievads():
    label["text"] = logs1.get()

btn1 = tk.Button(a, text="ievads", command=reizinajums)
btn1.grid(row=3, column=1)

btn2 = tk.Button(a, text="notirit", command=clear)
btn2.grid(row=3, column=2)

a.mainloop()