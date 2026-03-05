from turtle import *
krasa=[ "red", "green", "blue", "yellow","brown","lightblue","gray"]

def maja(x,y,a,c,d,b=90):
    pu()
    goto(x,y)
    down()
    color(c)
    fillcolor(c)
    begin_fill()
    for i in range (d):
        forward(a)
        left(b)
    end_fill()
maja(-100,-380,200,krasa[6],4) # Siena
maja(40,-50,40,krasa[5],4) 
maja(40,-10,40,krasa[5],4)
maja(40,30,40,krasa[5],4)
maja(40,70,40,krasa[5],4)
maja(-150,-180,300,krasa[4],3,120)
maja(0,-280,80,krasa[5],4)
maja(-90,-380,70,krasa[3],4)
maja(-90,-310,70,krasa[3],4)
maja(-15,-110,30,krasa[3],8,45)
mainloop()