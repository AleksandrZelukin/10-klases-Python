#Pirkuma kalkulators
summa = int(input("Ievadi summu: "))
cena = float(input("Ievadi cenu: "))
daudzums = int(input("Ievadi daudzumu: "))
real_daudzums = int(summa//cena)
truks = round(cena*daudzums - summa, 2)
atlikums = round(summa - int(summa//cena)*cena, 2)
if summa >= cena*daudzums:
    atlikums = round(summa - cena*daudzums, 2)
    print(f"Atlikums bus: {atlikums} eiro")
else:
    print ("Nav pietiekami naudas")
    print (f"Trukst: {truks} eiro")
    print(f"Tu vari nopirkt: {real_daudzums} kg. ābolus un atlikums bus: {atlikums} eiro")
