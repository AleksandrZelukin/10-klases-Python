'''
from tkinter import *

logs = Tk()
logs.geometry("600x600")
logs.title("10b klase logs") 
label1 = Label(text="Sveiki, Tkinter!")
 
label1.pack()

frame1=Frame(master=logs, width=100, height=100, bg="red" )
frame1.pack()



frame2=Frame(master=logs, width=100, height=100, bg="blue" )
frame2.pack()

label2 = Label(master=frame2, text="skolotajs!")
label2.pack()

logs.mainloop()

'''
import tkinter as tk

logs = tk.Tk()
logs.geometry("500x500")
 
label1 = tk.Label(text="Sveiki, Tkinter!",font="size 18")
 
label1.pack()

frame1=tk.Frame(master=logs, width=100, height=100, bg="red",bd=5 )
frame1.pack()

frame2=tk.Frame(logs, width=100, height=100, bg="blue" )
frame2.pack()

label2 = tk.Label(frame2, text="skolotajs!",font="size 14")
label2.pack()

frame3=tk.Frame(master=logs, width=200, height=50, bg="yellow")
frame3.pack()

label3=tk.Label(master=frame3, text="Skola", bg="yellow",bd=6)
label3.pack()

logs.tk.mainloop()

