from tkinter import *

a = Tk()
a.title("Manas pogas")
a.geometry("300x150+800+400")


entry = Entry(font="32")
entry.pack()

label50 = Label(font="32")
label50.pack()



def display():
    label["text"] = entry.get()

def clear():
    entry.delete(0, END)
    label["text"] = entry.get()
    
    
btn1 = Button(a, text="ievads", command=display)
btn2 = Button(a, text="notirit", command=clear)
btn3 = Button(a, text="iziet", command=exit)
btn1.place(relx=.2, rely=.4)
btn2.place(relx=.4, rely=.4)
btn3.place(relx=.6, rely=.4)

a.mainloop()

