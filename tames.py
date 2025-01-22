'''
https://siic-lv.github.io/programmesana/vidusskola/p1/specifikacija/#gridas-mainas-izmaksu-aprekinu-programma
Pasūtītājs Andris Ziediņš, remontē dzīvokļus un sagatavo tāmes. 
Andra draugs, kas ir programmētājs, 
izveidoja specifikāciju pēc Andra prasībām. 
Jūsu uzdevums ir uzrakstīt funkciju, 
kas no dotiem argumentiem aprēķina un atgriež Andrim derīgu rezultātu.
'''

import math

print("Cenas")
l = float(input("Lamināts(par paku),euro: "))
t = float(input("Tapetes(par rulli),euro: "))
k = float(input("Krāsa(par 1.litru),euro: "))
nauda = []
nauda.append(l)
nauda.append(t)
nauda.append(k)

#print(nauda)

def remonts(garums, augstums, platums):
    return math.ceil(garums*platums/2.131), math.ceil((garums+platums)*augstums/10), math.ceil((garums*platums)*0.4)

x = float(input("garums: "))
y = float(input("augstums: "))
z = float(input("platums:"))

tame = list(remonts(x,y,z))

#laminats = (tame[0])
#tapetes = (tame[1])
#krasa = (tame[2])

m=len(nauda)
i=0
kopa=[]
while i<m:
    kopa.append(nauda[i]*tame[i])
    i+=1
#print(kopa)
print("Laminata pirtkt: ", tame[0], "pakas")
print("Tapetes  pirtkt: ", tame[1], "rullus")
print("Krāsas pirtkt: ", tame[2], "litru")
print("Kopā jamāksā: ", round(sum(kopa),2),"Euro")

'''
2.	Pie jums ir vērsies uzņēmums SIA Stabili podesti, 
ar vēlmi atvieglot materiālu sagatavošanu finiera podestu ražošanai. 
Podestus ražo gan standarta izmēros, gan pēc pasūtītāja izmēriem.
Jūs uzaicina uz ražotni iepazīties ar produkciju, un var novērot, 
ka podesti principā ir taisnstūra paralēlskaldņi, 
kas izveidoti no sešām finiera plāksnēm, 
kas savā starpā sastiprināti ar divpadsmit leņķveida līstēm, 
un stūros nostiprināti ar astoņiem stūra savienojumiem.
Uzņēmums vēlas automatizēt izlietoto materiālu uzskaiti
un jums tiek uzticēts uzrakstīt kodu funkcijai, 
kas nosaka materiālu veidu un daudzumu dotā izmēra podestam.

SPECIFIKACIJA:
Funkcijai “materialuAprekins” ir četri parametri, 
saskaņā ar šo formātu: materialuAprekins(garums, platums, augstums, skaits). 
Parametri “garums”, “platums” un “augstums” raksturo podesta izmēru cm, 
tiem var būt arī viena zīme aiz komata. Parametrs “skaits” ir vesels skaitlis, 
kas norāda nepieciešamo podestu skaitu.
Uzskaites programmai informācija tiek nodota ar funkcijas “materialaUzskaite” palīdzību. 
Šī funkcija vēl nav pagatavota, un to rakstīs citi programmētāji. 
Šai funkcijai ir četri parametri, saskaņā ar šo formātu: 
materialaUzskaite(tips, izmers1, izmers2, skaits). 
Parametrs “tips” ir simbolu virkne, kam atļautas trīs vērtības: 
“FINIERIS”, “LISTE” un “STURIS”. Ja tips ir “FINIERIS”, 
tad parametri “izmers1” un” izmers2” apraksta taisnstūrveida finiera plāksnes izmērus, 
secība nav svarīga. Ja tips ir “LISTE”, tad parametrs “izmers1” 
apraksta līstes detaļas garumu, savukārt parametra “izmers2” 
vērtība nav svarīga. Ja tips ir “STURIS”, tad parametru 
“izmers1” un “izmers2” vērtības nav svarīgas.
Funkcijas “materialuAprekins” izpildes laikā ir jāizsauc funkcija 
“materialaUzskaite” ar nepieciešamajiem parametriem katram atšķirīgajam 
materiālu tipam un izmēram. Ideāli būtu, ja šo izsaukumu skaits būtu pēc iespējas mazāks.
'''

def materialuAprekins(garums, platums, augstums, skaits):

    return garums*platums*skaits

x=float(input("garums: "))
y=float(input("platums: "))
z=float(input("augstums: "))
r=int(input("skaits: "))

print(materialuAprekins(x,y,z,r))

liste = x
print("Liste daudzums:", 12*r)
sture = r*8
print("stures daudzums: ", sture)
finieris = r*x*y
print("Finiera nepiecešams:",finieris,"cm2")




