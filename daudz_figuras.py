from turtle import *
t = Turtle()
t.up()
def figura(x,y,s,n):
    t.goto(x,y)
    t.down()
    for i in range(n):
        t.forward(s)
        t.right(360/n)
    t.up()

figura(100,100,50,3)
figura(-100,-50,40,5)

t.screen.mainloop()