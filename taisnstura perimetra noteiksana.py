from tkinter import *

logs1 = Tk()
logs1.geometry("320x320")
lbl_1 = Label(text="Taisnsstura perimetrs")
lbl_1.pack()

num1 = Entry(width=10)
num1.pack()

btn1 = Button(text="+")
btn1.pack()

uzdevums = Label(text="Papildināt programmu\n ar trūkstošajiem blokiem,\n lai pabeigtu uzdevumu.",font=16,fg="red",bg="yellow")
uzdevums.pack()

logs1.mainloop()
