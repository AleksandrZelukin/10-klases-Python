from tkinter import *

a = Tk()
a.title("Manas pogas")
a.geometry("300x300+800+400")


entry = Entry(font="32")
entry.pack()

label50 = Label(text="50 centu monetas: ")
label50.pack()

label20 = Label(text="20 centu monetas: ")
label20.pack()

label10 = Label(text="10 centu monetas: ")
label10.pack()

label5 = Label(text="5 centu monetas: ")
label5.pack()

label2 = Label(text="2 centu monetas: ")
label2.pack()

label1 = Label(text="1 centu monetas: ")
label1.pack()


def display():
    label["text"] = entry.get()

def clear():
    entry.delete(0, END)
    label["text"] = entry.get()
    
    
btn1 = Button(a, text="ievads", command=display)
btn2 = Button(a, text="notirit", command=clear)
btn3 = Button(a, text="iziet", command=exit)
btn1.place(relx=.2, rely=.8)
btn2.place(relx=.4, rely=.8)
btn3.place(relx=.6, rely=.8)

a.mainloop()