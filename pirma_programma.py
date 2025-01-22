'''
Pirma programma 10.b klase
'''

from math import pi #importejam no modula math pi

print("Sveiki! Ka tevi sauc, draugs?")
name = input()
print("Sveiki ", name)
print("ievadi tainsstura malas:")
a = int(input("a= "))
b = int(input("b= "))
s = a*b

print("Tainsstura platiba ir: ",s," ",name)
print("Tainsstura platiba ir:{}".format(s),  " ",name)


print("ievadi radiuss:")
r = int(input("radiuss= "))

s = pi*r**2
print("Apļa platiba ir: ",s, " ",name)
print("Apļa platiba ir: ",round (s,4), " ",name)
print("Apļa platiba ir:{0:.4f}".format(s))


