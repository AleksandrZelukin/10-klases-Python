from tkinter import *
import turtle as tu
logs = Tk()
logs.title("Manas pirmas pogas")
logs.geometry("480x480+800+400")


entry1 = Entry(font="48")
entry1.place(relx=.4, rely=.1)
def a():
    label1["text"] = entry1.get()
def b():
    label1["text"] = " "
def c():
    tu.fd(200)

btn1 = Button(text="Poga",command=a)
btn1.place(relx=.2, rely=.2)
label1 = Label(font="48")
label1.place(relx=.3, rely=.2)
btn2 = Button(text="Izdzest",command=b)
btn2.place(relx=.4, rely=.2)
btn2 = Button(text="Poga C",command=c)
btn2.place(relx=.5, rely=.2)
btn3 = Button(text="Izeja",bg="red",fg="yellow",width=20,height=5,command=exit)
btn3.place(relx=.35,rely=0.8)
logs.mainloop()
