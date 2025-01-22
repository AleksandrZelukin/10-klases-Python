'''
a = int(input("a: "))
b = int(input("b: "))

if a>b:
    x = b
    y = a
else:
    x = a
    y = b  

print("virkne no maz. līdz liel.: ",x,y)
print(f"{x} mazāk {y}")
print("{} mazāk {}".format(x,y))
'''
L = int(input("Man kabatā ir: "))
C = float(input("Aboli maksa: "))
M = int(input("Grību pirkt(kg.): "))

S = L - (M*C)
if S<0:
    print("Maz nauda")
else:
    print("Atlikums bus: ",round(S,2))