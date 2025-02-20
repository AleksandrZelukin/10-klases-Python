import turtle
import tkinter

a = turtle.Screen()
a.setup(800,800)

def kvadrats():
    for i in range(4):
        turtle.fd(200)
        turtle.lt(90)

# loadimage = tkinter.PhotoImage(file="kvadratik.png")


        
btn_kvadrat=tkinter.Button(text="kvadrats",command=kvadrats)
btn_kvadrat.place(x=120,y=100)

turtle.mainloop()