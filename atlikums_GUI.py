from tkinter import *

a = Tk()
a.title("Manas pogas")
a.geometry("300x300+800+400")

entry = Entry(font="32")
entry.pack()
label = Label()
label.pack()

def display():
    a = int(entry.get())//50
    b = (int(entry.get())-a*50)//20
    c = (int(entry.get())-a*50-b*20)//10
    d = (int(entry.get())-a*50-b*20-c*10)//5
    e = (int(entry.get())-a*50-b*20-c*10-d*5)//2
    f = (int(entry.get())-a*50-b*20-c*10-d*5-e*2)//1
    kopa = a+b+c+d+e+f
    label["text"] = (f""" 50 centu monetas: {a}\n 
    20 centu monetas: {b}\n 
    10 centu monetas: {c}\n 
    5 centu monetas: {d}\n 
    2 centu monetas: {e}\n 
    1 centu monetas: {f}\n
    Kopā: {kopa} monetas""")
    
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