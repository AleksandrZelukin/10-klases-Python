'''

Kreklu apdruka
Problēma

Draugiem jāaprēķina, cik izmaksās apdrukātu T-kreklu pasūtīšana un piegāde, 
ņemot vērā, ka cena ir atkarīga no apdrukas veida un kreklu skaita, 
bet piegādes maksa ir atkarīga no pasūtījuma summas.

Specifikācija

●  Funkcijai pasuti_tkreklus ir trīs parametri saskaņā ar formātu pasuti_tkreklus(skaits,apdruka, piegade). 
Parametrs skaits ir vesels skaitlis(pasūtamo kreklu skaits), 
parametri apdruka un piegade ir simbolu virknes.
●  Parametrs apdruka var būt simbolu virkne, kam atļautas trīs vērtības:TEKSTS, ZIME vai FOTO. 
Cena attiecīgi ir 5 EUR, 7 EUR un 20 EUR.
●  Parametrs piegade ir Būla tipa mainīgais (True vai False). 
Ja piegade ir True un kopējā pasūtījuma summa ir mazāka nekā 50 EUR, par piegādi papildus jāmaksā 15 EUR, 
ja summair 50 EUR vai vairāk, tad piegāde ir par brīvu.
●  Pasūtījumiem, kas pārsniedz 100 EUR, tiek piemērota 5 % atlaide no pasūtījuma summas


def pasuti_tkreklus(skaits,apdruka, piegade):
    skaits = int(input("ievadi kreklus daudzumu: "))
    apdruka = {"teksts":5, "zime":7, "foto":20}
    piegade = [True, False]
'''

s = int(input("ievadi kreklus daudzumu: "))
a = input("""Ievadi apdrukas veidu: 
teksts - 5 EUR 
zime - 7 EUR 
foto - 20 EUR\n""") 
if a == 'teksts':
    apdruka = s*5
if a == 'zime':
    apdruka = s*7
if a == 'foto':
    apdruka = s*20

piegade = input("Piegadāt pasūtījumu? y/n\n")
if piegade == 'y' and apdruka <50:
    apdruka +=15
    print("Jūsu pasūtijums māksā {} EUR".format(apdruka))
elif piegade == 'y' and apdruka <100:
    print("Jūsu pasūtijums māksā {} EUR".format(apdruka))
elif piegade == 'y' and apdruka >100:
    apdruka -=apdruka*0.05
    print("Jūsu pasūtijums māksā {} EUR".format(apdruka))
else: print("Jūsu pasūtijums māksā {} EUR".format(apdruka))

print("Jūsu pasutijums satav no {} kreklus ar apdruku ar {} formātu".format(s,a))
print("Paldies, ka izmantojiet musu pakalpojumu!")