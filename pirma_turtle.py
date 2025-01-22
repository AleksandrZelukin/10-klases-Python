from turtle import *
a = Turtle()

a.shape("square")
a.pencolor("red")
a.fillcolor("yellow")
a.pensize(4)

a.begin_fill()
for i in range(4):
    a.forward(100)
    a.right(90)
    
a.end_fill()
a.up()
a.goto(-200,100)
a.down()
a.fillcolor("blue")
a.begin_fill()
for i in range(5):
    a.forward(100)
    a.left(72)
a.end_fill() 

a.screen.mainloop()