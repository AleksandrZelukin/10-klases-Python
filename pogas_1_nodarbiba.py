from tkinter import *
a = Tk()
# a.title("mana pirma poga")
a.geometry("600x600+550+100")

def pirma():
    label.configure(text="Sveiki, draugs!")
def otra():
    print("Ka iet?")
def close():
   a.destroy()

l1 = Label(text="Welcome")
l1.pack()

e=Entry()
e.pack()

b1 = Button(text="Pirma poga", background = "blue", foreground="yellow", command = pirma)
b2 = Button(text="Otra poga", background = "red", foreground="yellow", command=otra)
b3 = Button(text="Otra poga", background = "magenta", foreground="yellow", command=close)


b1.pack(expand=True)
label=Label(a)
label.place(x=40, y=50)
b2.pack(expand=True)
b3.pack(expand=True)

a.mainloop()
