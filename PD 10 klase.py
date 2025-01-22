'''
Programma pieprasa kvadrāta mālu a un izskaitļo perimetru (2.punkti)
Programma pieprasa Kārļa trīs atzīmes un izskaitļo vidējo aritmētisko. (2.punkti)
Kārlis noperka M kg abolu maksājot C centus par kg. Cik centus X ir jāsamaksa par pirkumu?
Cik atlikuma centus S viņš dabūs no L eiro? (4.punkti)
Annai ir a gadi, bet Marutai - m gadi. Kas no viņam ir vecāka? (2.punkti)
Pļavā rotaļājas bērni un suņi. Zinot galvu un kāju kopējo skaitu (g un k),
atrast, cik bērnu un cik suņu ir pļavā (b un s). (6.punkti)
Zinot kuba mālu a, aprēķināt kuba tilpumu, tā virsmas laukumu un diagonāles garumu.
'''
#1 
a = int(input("Ievadiet kvadrata malu: "))
p=a*4
print("Kvadrata perimetrs ir:",p )

#2
a1 = int(input("Pirma atzime: "))
a2 = int(input("Otra atzime: "))
a3 = int(input("Tresa atzime: "))

v=(a1+a2+a3)/3

print("videja atzime ir:",v)

#3

L = int(input("Nauda kopa (euro):"))
M = int(input("noperka aboli kg:"))
C = float(input("cena par kilo (euro): "))
x=L-(M*C)
print("samaksa: ",C*M," euro")
print("atlikums:",x, "euro")

#4
Anna = int(input("Annai:"))
Maruta = int(input("Marutai:"))
if Anna > Maruta:
    print("Anna vecaka Marutai")
else:
    print("Maruta vecaka Annai")
    
#5 Pļavā rotaļājas bērni un suņi. Zinot galvu un kāju kopējo skaitu (g un k),
#atrast, cik bērnu un cik suņu ir pļavā (b un s)
g = int(input("Galvas: "))
k = int(input("Kājas: "))
x=k-(g*2) #"liekas"kajas
s=x/2 #suņu skaits
b=g-s #bernus skaits
print("suņus skaits: ", s)
print("bernus skaits: ", b)

#5 Zinot kuba mālu a,
#aprēķināt kuba tilpumu,
#tā virsmas laukumu un diagonāles garumu.

a = int(input("Kuba mala: "))
v = a**3

print("kuba tilpums: ", v)
d1 = a*1.77
d2 = a*1.44
print("kuba diagonāles: ", d1, d2)
