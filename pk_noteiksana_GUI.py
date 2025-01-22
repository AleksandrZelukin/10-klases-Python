from tkinter import *
from datetime import *
a = Tk()
a.title("Manas pogas")
a.geometry("300x300+800+400")
vards1=Label(text="Vārds, Uzvārds")
vards1.pack()
vards = Entry(font="32")
vards.pack()
personas_kods1 = Label(text="personas kods")
personas_kods1.pack()
personas_kods = Entry(font="32")
personas_kods.pack()
label = Label(font="32")
label.pack()
label_y = Label(font="32")
label_y.pack()
label_m = Label(font="32")
label_m.pack()
label_d = Label(font="32")
label_d.pack()
def display():
    label["text"] = (vards.get() + " " + personas_kods.get())
    pk = personas_kods.get()
    pk1 = list(pk)
    if pk[7]=="1":
        pk1.insert(4,"19")
    elif pk[7]=="2":
        pk1.insert(4,"20")
    try:
        dd = (''.join(pk1[0:7]))
        dz=datetime.strptime(dd,"%d%m%Y")
        label_y.configure(text = dz.year)
        label_m.configure(text= dz.month)
        label_d.configure(text= dz.day)
    except:
        label_y.configure(text="Nepareizi dzimšanas dati.")
def clear():
    vards.delete(0, END)
    personas_kods.delete(0, END)
    label["text"] = vards.get()
 
     
btn1 = Button(a, text="ievads", command=display)
btn2 = Button(a, text="notirit", command=clear)
btn3 = Button(a, text="iziet", command=exit)
btn1.place(relx=.2, rely=.8)
btn2.place(relx=.4, rely=.8)
btn3.place(relx=.6, rely=.8)

a.mainloop()