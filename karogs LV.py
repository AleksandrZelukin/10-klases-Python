from turtle import *

t = Turtle()
t.up()

t.goto(-250,125)
t.down()
t.color('#9D2235')
t.begin_fill()
for i in range(2):
    t.forward(500)
    t.right(90)
    t.forward(250)
    t.right(90)
t.end_fill()

t.up()
t.goto(-250, 25)

t.color('#ffffff')
t.down()
t.begin_fill()
for i in range(2):
    t.forward(500)
    t.right(90)
    t.forward(50)
    t.right(90)
t.end_fill()
t.up()
t.goto(0,-15)
t.down()
t.color('#9D2235')
t.hideturtle()
t.write("Manai Latvijai - 104!", move=False, align='center', font=('Helvetica', 18, 'italic')) 
t.screen.mainloop()