'''
https://siic-lv.github.io/programmesana/vidusskola/p1/specifikacija/
Specifikacija:
Nepieciešama iespēja definēt recepti un tās sastāvdaļas
Nepieciešama iespēja definēt, cik maksā katra sastāvdaļa
Sistēmai jāaprēķina kopējās ievārījuma izmaksas, balstoties uz ievadīto ābolu apjomu
un cukura cenu par vienu kg
'''
cukur = float(input("Cukura cena: "))
aboli = float(input("Āboli: "))
def ievarijums(aboli_svars, cukurs_uz_kg):
    cukura_cena = cukur
    izmaksa_kg = round((cukura_cena * cukurs_uz_kg),2)
    return izmaksa_kg * aboli_svars

cukurs = round((aboli*0.6),2)
print(f"Uz {aboli} kg ābolu ir nepicešams {cukurs} kg cukura")
print("Un izmaksas būs {} EUR".format(ievarijums(aboli, cukurs)))