from turtle import *
pencolor("red")
pensize(6)
speed(2)
shape("square")
hideturtle()
fillcolor("blue")

def draw_square(a, b):
    penup()
    goto(a, b)
    pendown()
    begin_fill()
    for i in range(n):
        fd((125/n)*4)
        lt(360/n)
    end_fill()
x = int(input("Enter x coordinate: "))
y = int(input("Enter y coordinate: "))
n = int(input("Enter number of sides: "))
draw_square(x, y)

mainloop()