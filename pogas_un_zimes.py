import turtle
import tkinter
krasa = ["red","blue","orange","green","yellow"]
a = turtle.Screen()
a.setup(800,800)

def kvadrats():
    turtle.clear()
    turtle.fillcolor(krasa[0])
    turtle.begin_fill()
    for i in range(4):
        turtle.fd(200)
        turtle.lt(90)
    turtle.end_fill()

def triangle():
    turtle.clear()
    turtle.fillcolor(krasa[1])
    turtle.begin_fill()
    for i in range(3):
        turtle.fd(200)
        turtle.lt(120)
    turtle.end_fill()

btn_kvadrat=tkinter.Button(text="kvadrats",width=15,command=kvadrats)
btn_kvadrat.place(x=120,y=100)
btn_tr=tkinter.Button(text="trijsturis",width=15,command=triangle)
btn_tr.place(x=120,y=140)
btn_iz=tkinter.Button(text="izeja",width=15,command=exit)
btn_iz.place(x=120,y=180)
turtle.mainloop()