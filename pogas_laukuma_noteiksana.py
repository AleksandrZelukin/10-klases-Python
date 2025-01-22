import tkinter as tk
win = tk.Tk()
win.title("Kalkulators")
win.geometry("300x400")
num1 = tk.Entry(win)
num1.place(relx=.2, rely=.1)
num2 = tk.Entry(win)
num2.place(relx=.2, rely=.2)
res = tk.Label(win, text = "=")
res.place(relx=.2, rely=.4)
nos = tk.Label(win, text = "Ievādu skaitļus lodziņā")
nos.place(relx=.2, rely=.0)
'''
def temp_text(e):
   entry.delete(0,"end")

num1.bind("<FocusIn>", temp_text)
num1.pack()

def summation():
    one = float(num1.get())
    two = float(num2.get())
    result = one + two
    res.configure(text = "= %s" % result)
'''
def reizinajums():
    one = float(num1.get())
    two = float(num2.get())
    result = one * two
    res.configure(text = "= %s" % result)
'''
button1 = tk.Button(win, text = "summa",
                    background="#FF00AA",
                    foreground="#0000AA",
                    activebackground="#00FF00",
                    command = summation)
button1.place (relx=.2, rely=.3)
'''
button1 = tk.Button(win, text = "reizinājums",
                    background="#FF00AA",
                    foreground="#0000AA",
                    activebackground="#00FF00",
                    command = reizinajums)
button1.place (relx=.4, rely=.3)

win.mainloop()

