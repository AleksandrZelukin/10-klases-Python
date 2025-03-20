x = int(input("Ievadi skaitli x: "))
y = int(input("Ievadi skaitli y: "))
z = x + y 
print(z)

a = open("saraksts.txt", "a",encoding="utf-8")

print(z,file=a)
a.close()