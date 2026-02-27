from turtle import *
shapesize(1, 1, 1)
shape("turtle")
krasa=["blue", "red", "green", "yellow","purple","orange"]
speed(4)
pensize(6)
def draw_square(krasa,vieta):
    penup()
    goto(vieta)
    pendown()
    color(krasa)
    fillcolor(krasa)
    begin_fill()
    for i in range(4):
        forward(100)
        right(90)
    end_fill()
draw_square(krasa[0], (0, -200))
draw_square(krasa[1], (100, -100))
draw_square(krasa[2], (0, 0))
draw_square(krasa[3], (100, 100))
draw_square(krasa[4], (0, 200))
draw_square(krasa[5], (100, 300))

mainloop()