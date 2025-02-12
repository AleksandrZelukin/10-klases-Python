from turtle import *
up()
goto(-100,-100)
down()
a=int(input("Cik malu?: "))
for i in range(a):
    fd(50)
    lt(360/a)
mainloop()