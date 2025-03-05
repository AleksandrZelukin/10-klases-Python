atlikums = int(input("ievadiet atlikumu summu: "))

kassa = (50,20,10,5,2,1)

a = atlikums//50
b = (atlikums-a*50)//20
c = (atlikums-a*50-b*20)//10
d = (atlikums-a*50-b*20-c*10)//5
e = (atlikums-a*50-b*20-c*10-d*5)//2
f = (atlikums-a*50-b*20-c*10-d*5-e*2)//1

print(f"""Lai izdot atlikumu {atlikums} centu, nepiecešams 
      {a} monetas pa {kassa[0]}, 
      {b} monetas pa {kassa[1]}, 
      {c} monetas pa {kassa[2]}, 
      {d} monetas pa {kassa[3]},
      {e} monetas pa {kassa[4]} un 
      {f} monetas pa {kassa[5]} centu""")

atlikums = int(input("Ievadiet atlikumu summu: "))

kassa = (50, 20, 10, 5, 2, 1)

monetas = []

for j in kassa:
    count = atlikums // j
    monetas.append(count)
    atlikums %= j

print(f"Lai izdot atlikumu {atlikums} centu, nepieciešams:")
for i, j in enumerate(kassa):
    print(f"{monetas[i]} monētas pa {j} centiem")