from random import randint
from tkinter import *
logs = Tk()
logs.title("Atzīmes ģenerators")
logs.geometry("500x300+800+400")
f = open("atzimes_10b_II_sem.txt", "a", encoding=("utf-8"))
uzv = Entry( font=("Arial", 16))
uzv.pack()

def atzime():
    atzime1 = randint(0,10)
    atzime2 = randint(0,10)
    atzime3 = randint(0,10)
    atzime = str(round(((atzime1 + atzime2 + atzime3)/3),0))
    vards = uzv.get()
    rez = vards +" "+ atzime
    atz.configure(text ="Vidēja atzīme ir: " + atzime)
    print(rez, file=f)
    
poga1 = Button(text="Ģenerēt atzimi un sūtit registrā",command=atzime)
poga1.pack()

atz = Label(text="", font=("Arial", 32))
atz.pack()


logs.mainloop()