from tkinter import *
from tkinter import messagebox
import json

# ---------- logs ----------
logs = Tk()
logs.title("Reģistrācijas forma")
logs.geometry("600x400")
logs.resizable(False, False)

# ---------- functions ----------
def registracija():
    dati = {
        "vards": entry1.get(),
        "uzvards": entry2.get(),
        "talrunis": entry3.get(),
        "pilseta": entry4.get(),
        "iela": entry5.get(),
        "dzivoklis": entry6.get()
    }

    # pārbaude: vai visi lauki aizpildīti
    for lauks in dati.values():
        if lauks == "":
            messagebox.showerror("Kļūda", "Lūdzu, aizpildiet visus laukus!")
            return

    # saglabāšana JSON failā
    try:
        with open("registracija.json", "a", encoding="utf-8") as f:
            json.dump(dati, f, ensure_ascii=False)
            f.write("\n")
        messagebox.showinfo("Gatavs", "Dati veiksmīgi saglabāti!")
        notirit()
    except:
        messagebox.showerror("Kļūda", "Neizdevās saglabāt failu!")

def notirit():
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)
    entry6.delete(0, END)

# ---------- labels & entries ----------
Label(text="Lūdzu, reģistrēties", font=("Arial", 16)).place(relx=0.33, rely=0.02)

Label(text="Vārds").place(relx=0.05, rely=0.12)
entry1 = Entry(width=25)
entry1.place(relx=0.25, rely=0.12)

Label(text="Uzvārds").place(relx=0.05, rely=0.2)
entry2 = Entry(width=25)
entry2.place(relx=0.25, rely=0.2)

Label(text="Tālruņa numurs").place(relx=0.05, rely=0.28)
entry3 = Entry(width=25)
entry3.place(relx=0.25, rely=0.28)

Label(text="Pilsēta").place(relx=0.05, rely=0.36)
entry4 = Entry(width=25)
entry4.place(relx=0.25, rely=0.36)

Label(text="Iela").place(relx=0.05, rely=0.44)
entry5 = Entry(width=25)
entry5.place(relx=0.25, rely=0.44)

Label(text="Dzīvoklis").place(relx=0.05, rely=0.52)
entry6 = Entry(width=25)
entry6.place(relx=0.25, rely=0.52)

# ---------- buttons ----------
Button(text="Saglabāt datus", width=20, command=registracija).place(relx=0.25, rely=0.62)
Button(text="Notīrīt laukus", width=20, command=notirit).place(relx=0.25, rely=0.7)

logs.mainloop()
