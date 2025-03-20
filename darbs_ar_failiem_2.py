import pickle

x = int(input("Ievadi skaitli x: "))
y = int(input("Ievadi skaitli y: "))
z = x**y
print(z)

a = open("saraksts2.data", "wb")
pickle.dump(z,a)
a.close() 
print("Dati ir ierakstīti failā")
a = open("saraksts2.data", "rb")
b=pickle.load(a)
print(b)
a.close()