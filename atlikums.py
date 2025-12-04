atlikums = int(input("ievadiet atlikumu summu: "))

kassa = (50,20,10,5,2,1)

a = atlikums//50
b = (atlikums-a*50)//20
c = (atlikums-a*50-b*20)//10
d = (atlikums-a*50-b*20-c*10)//5
e = (atlikums-a*50-b*20-c*10-d*5)//2
f = (atlikums-a*50-b*20-c*10-d*5-e*2)//1

print(f"Lai izdot atlikumu {atlikums} centu, nepiecešams") 
if a != 0:
      print(f"{a} monetas pa {kassa[0]}")
if b != 0:
      print(f"{b} monetas pa {kassa[1]}")
if c != 0:
      print(f"{c} monetas pa {kassa[2]}")
if d != 0:
      print(f"{d} monetas pa {kassa[3]}")
if e != 0:
      print(f"{e} monetas pa {kassa[4]}")
if f != 0:
      print(f"{f} monetas pa {kassa[5]}")


