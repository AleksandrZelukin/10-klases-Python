import math

h = float(input("platums: "))
b = float(input("garums: "))
cc = float(input("Augstums: "))
Linoleja_cena = float(input("Linolēja cena: "))
rulla_cena = float(input("Tapetes cena: "))
perimetrs = 2*(h+b)

tapetes_daudzums = math.ceil((perimetrs/0.5/cc) - 1)
tapetes_cena = round(rulla_cena*tapetes_daudzums,2)

linoleja_daudzums = h*b
linolejs_kopa = linoleja_daudzums*Linoleja_cena
print(f"Kopejais tapetes daudzums ir: {tapetes_daudzums} ruļļus ar kopēja cenu {tapetes_cena} EUR")
print(f"Kopejais linoleja daudzums ir: {linoleja_daudzums} m2 ar kopēja cenu {linolejs_kopa} EUR")