from tkinter import Tk, Label, Entry, Button

logs = Tk()
logs.geometry("150x200+800+400")

l1=Label(text="Taisnstura 1.mala")
l1.pack()
e1 = Entry()
e1.pack()

l2=Label(text="Taisnstura 2.mala")
l2.pack()
e2 = Entry()
e2.pack()

def close():
    logs.destroy()

def reizinajums():
    one = float(e1.get())
    two = float(e2.get())
    result = one * two
    res.configure(text = "= %s" % result)

btn1 = Button(text="Taisnstura laukums", command=reizinajums)
btn1.pack()
res = Label(text = "=")
res.pack()
btn2 = Button(text="iziet", command=close)
btn2.pack()


logs.mainloop()