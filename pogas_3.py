from tkinter import *
logs = Tk()
logs.title("Manas pirmas pogas")
logs.geometry("480x600+800+400")
# programmas sakums
def ievadit():
    a = open("pogas_3.txt","a",encoding="utf-8")
    lab2.config(text=(entry1.get(),"Uzrākstits datnē"))
    print(entry1.get(), file=a)
    a.close()
def notirit():
    entry1.delete(0, END)
    lab2.config(text="")
def atjaunot_lab3():
    try:
        with open("pogas_3.txt", "r", encoding="utf-8") as f:
            saturs = f.read()
            lab3.config(text=saturs)
    except FileNotFoundError:
        lab3.config(text="Datne nav atrasta.")
lab1 = Label(logs, text="Mana pirma programma",font=("Arial", 24))
lab1.pack()
entry1 = Entry(font=("Arial", 24))
entry1.pack()
lab2 = Label(logs, text="",font=("Arial", 24))
lab2.pack()
btn1 = Button(logs, text="Ievadīt",bg="green",fg="white", font=("Arial", 16),command=ievadit)
btn1.pack()
btn2 = Button(logs, text="Notīrīt",bg="blue",fg="white", font=("Arial", 16),command=notirit)
btn2.pack()
btn = Button(logs, text="Iziet no programmas",bg="red",fg="white", font=("Arial", 16),command=logs.quit)
btn.pack()
btn4 = Button(logs, text="Skatīt", bg="orange", fg="black", font=("Arial", 16), command=atjaunot_lab3)
btn4.pack()
lab3 = Label(logs, text="",font=("Arial", 12))
lab3.pack() 
logs.mainloop()