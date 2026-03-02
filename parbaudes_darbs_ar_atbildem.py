# ======================================================
# 1. uzdevums (10 punkti)
# Izveidot funkciju skaitlu_summa(saraksts), 
# kas atgriež visu skaitļu summu.
# Piemērs:
# saraksts = [3, 7, 2] → rezultāts: 12

saraksts = [6,3,12,8,19]

def skaitlu_summa(saraksts):
    s = 0
    for x in saraksts:
        s = s + x
    return s
print(skaitlu_summa(saraksts))

# ======================================================
# 2. uzdevums (10 punkti)
# Izveidot funkciju pozitivi_skaitli(saraksts), 
# kas atgriež tikai pozitīvos skaitļus.
# Piemērs:
# saraksts = [-2, 5, 0, 8, -1] → rezultāts: [5, 8]
def pozitivi_skaitli(saraksts):
    jauns = []
    for x in saraksts:
        if x > 0:
            jauns.append(x)
    return jauns
print(pozitivi_skaitli(saraksts))
# ======================================================
# 3. uzdevums (10 punkti)
# Izveidot funkciju maksimalais(saraksts), neizmantojot max().
def maksimalais(saraksts):
    lielakais = saraksts[0]
    for x in saraksts:
        if x > lielakais:
            lielakais = x
    return lielakais

print(maksimalais(saraksts))
# ======================================================
# 4. uzdevums (10 punkti)
# Ievadīt 5 skaitļus, saglabāt sarakstā un izvadīt summu, 
# pozitīvos skaitļus un lielāko skaitli.
skaitli = []
for i in range(5):
    sk = int(input('Ievadi skaitli: '))
    skaitli.append(sk)

print(skaitlu_summa(skaitli))
print(pozitivi_skaitli(skaitli))
print(maksimalais(skaitli))
# ======================================================
# 5. uzdevums (10 punkti)
# Izveidot funkciju videjais(saraksts), 
# kas aprēķina vidējo aritmētisko.
def videjais(saraksts):
    summa = 0
    for x in saraksts:
        summa = summa + x
    return summa / len(saraksts)

print(videjais(skaitli))
# 
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Vērtēšanas kritēriji
# Katram uzdevumam:
# • 10 punkti – uzdevums izpildīts pareizi, funkcija darbojas.
# • 7–9 punkti – nelielas kļūdas, bet loģika pareiza.
# • 4–6 punkti – daļēji pareizs risinājums.
# • 1–3 punkti – mēģinājums, bet funkcija nestrādā.
# • 0 punkti – nav risinājuma.
