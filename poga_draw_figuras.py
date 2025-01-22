import tkinter as tk
import turtle as tu
import random

logs = tu.Screen()
logs.setup(800,600)
tu.pensize(4)
tu.shape('turtle')
tu.speed(10)
krasa = ['red','pink','yellow','blue','green','orange']

def zvaigzne():
    tu.clear()
    tu.up()
    tu.home()
    tu.goto(-50,50)
    tu.down()
    random.shuffle(krasa)
    tu.color(krasa[0])
    tu.fillcolor(krasa[1])
    tu.begin_fill()
    for i in range(5):
        tu.fd(150)
        tu.lt(216)
    tu.end_fill()

def kvadrat():
    tu.clear()
    tu.up()
    tu.home()
    tu.goto(-50,-50)
    tu.down()
    random.shuffle(krasa)
    tu.color(krasa[0])
    tu.fillcolor(krasa[1])
    tu.begin_fill()
    for i in range(4):
        tu.fd(100)
        tu.lt(90)
    tu.end_fill()

def trijsturis():
    tu.clear()
    tu.up()
    tu.home()
    tu.goto(-50,-50)
    tu.down()
    random.shuffle(krasa)
    tu.color(krasa[0])
    tu.fd(100)
    tu.lt(90)
    tu.fd(200)
    tu.goto(-50,-50)
    # for i in range(3):
    #     tu.fd(100)
    #     tu.lt(120)

def aplis():
    tu.clear()
    tu.up()
    tu.home()
    tu.goto(0,-50)
    tu.down()
    random.shuffle(krasa)
    tu.color(krasa[0])
    tu.circle(100)

def notirit():
    tu.clear()

btn_zvaigzne=tk.Button(text="Zvaigzne",command=zvaigzne)
btn_kvadrat=tk.Button(text="Kvadrats",command=kvadrat)
btn_trijstur=tk.Button(text="Trijsturis",command=trijsturis)
btn_aplis=tk.Button(text="Aplis",command=aplis)
btn_clear=tk.Button(text="Notirit viss",command=notirit)
btn_zvaigzne.place(x=20,y=60)
btn_kvadrat.place(x=20,y=100)
btn_trijstur.place(x=20,y=140)
btn_aplis.place(x=20,y=180)
btn_clear.place(x=20,y=240)

tu.mainloop()