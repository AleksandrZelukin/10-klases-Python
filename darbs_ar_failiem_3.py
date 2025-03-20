import json

x = int(input("Ievadi skaitli x: "))
y = int(input("Ievadi skaitli y: "))
z = x+y
print(z)

a = open("saraksts3.txt", "w")
json.dump(z,a)
a.close()
print("Dati ir ierakstīti failā")
a = open("saraksts3.txt", "r")
b=json.load(a)
print(b)
a.close()