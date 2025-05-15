# Nolasa skaitļu skaitu
n = int(input("Ievadi skaitļu skaitu: "))

# Nolasa pašus skaitļus, pārveidojot tos sarakstā ar int tipa elementiem
skaitli = list(map(int, input("Ievadi skaitļus atdalītus ar atstarpi: ").split()))

# Filtrē pāra skaitļus, kas lielāki par 10
atlase = [x for x in skaitli if x % 2 == 0 and x > 10]

# Izvada rezultātu
if atlase:
    print(" ".join(map(str, atlase)))
else:
    print("Nav neviena")
# pāra skaitļa, kas lielāks par 10")