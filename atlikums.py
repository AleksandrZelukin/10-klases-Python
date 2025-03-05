atlikums = int(input("ievadiet atlikumu summu: "))

kassa = (50,20,10,5,2,1)

a = atlikums//50
b = (atlikums-a*50)//20
c = (atlikums-a*50-b*20)//10
d = (atlikums-a*50-b*20-c*10)//5
e = (atlikums-a*50-b*20-c*10-d*5)//2
f = (atlikums-a*50-b*20-c*10-d*5-e*2)//1

print(f"""Lai izdot atlikumu {atlikums} centu, nepiecešams 
      {a} monetas pa 50, 
      {b} monetas pa 20, 
      {c} monetas pa 10, 
      {d} monetas pa 5,
      {e} monetas pa 2 un 
      {f} monetas pa 1 centu""")

