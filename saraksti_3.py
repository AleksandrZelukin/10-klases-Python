a = []

b = int(input("Ievadi skaitli: "))


while b!=0:
    b = int(input("Ievadi skaitli: "))
    a.append(b)
    if b==0:
        break
    
print(a)