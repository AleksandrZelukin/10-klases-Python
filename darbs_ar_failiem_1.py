x = int(input("Ievadi skaitli x: "))
y = int(input("Ievadi skaitli y: "))
z = x + y 
print(z)
z = x + y

a = open("saraksts.txt", "w",encoding="utf-8")

print(z,file=a)
a.close()

a = open("saraksts.txt", "r",encoding="utf-8")

b = int(a.read())
s = int(input("Ievadi skaitli s: "))
s = s + b

# print(a.read())

print(s)
a = open("saraksts.txt", "a",encoding="utf-8")
print(s,file=a)
a.close()