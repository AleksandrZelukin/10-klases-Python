import turtle

logs1 = turtle.screen()

logs2 = Turtle()
logs1.pensize(4)

logs1.shape("turtle")
krasa = ["red","yellow","blue","green","orange"]
logs1.up()
logs1.goto(-240,-380)
logs1.down()
logs1.fillcolor(krasa[0])
a=4
logs1.begin_fill()
for i in range(a):
    logs1.fd(500)
    logs1.lt(360/a)
logs1.end_fill()
logs2 = Turtle()
logs2.up()
logs2.goto(-260,120)
logs2.down()
logs2.fillcolor(krasa[1])
a=3
logs2.begin_fill()
for i in range(a):
    logs2.fd(540)
    logs2.lt(360/a)
logs2.end_fill()
mainloop()