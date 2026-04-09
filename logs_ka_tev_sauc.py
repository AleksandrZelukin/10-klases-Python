from tkinter import *

logs = Tk()
logs.geometry("600x600+500+200")
logs.title("programma 'Ka tev sauc?'")

def atbilde():
    atb["text"] = atb.get()
    lb2.config(text=("Sveiki",atb.get()))

lb1 = Label(text = "Sveiki, draugs! Ka tevi sauc?", font=('Helvetika',24,'bold'))
lb1.pack(padx=20,pady=20)
atb = Entry(font=('Helvetika',24,'bold'))
atb.pack(padx=20,fill=X,pady=20)
btn = Button(text="Nospiež mani!",font=('Helvetika',24,'bold'),command=atbilde)
btn.pack(padx=20,pady=20)
lb2 = Label(text = " ",font=('Helvetika',24,'bold'))
lb2.pack(padx=20,pady=40,fill=X)
btn_izeja = Button(text="Iziet",bg='red',font=('Helvetika',24,'bold'),command=logs.destroy)
btn_izeja.pack(side=BOTTOM)

logs.mainloop()
