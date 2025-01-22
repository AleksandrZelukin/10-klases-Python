'''
https://siic-lv.github.io/programmesana/vidusskola/p1/specifikacija/
Specifikacija:
Nepieciešama iespēja definēt recepti un tās sastāvdaļas
Nepieciešama iespēja definēt, cik maksā katra sastāvdaļa
Sistēmai jāaprēķina kopējās ievārījuma izmaksas, balstoties uz ievadīto ābolu apjomu
'''

def ievarijums(aboli_svars, cukurs_uz_kg):
    cukura_cena = 0.75
    izmaksa_kg = cukura_cena * cukurs_uz_kg
    return izmaksa_kg * aboli_svars

aboli = 1.7
cukurs = 0.9
print("Uz {} kg ābolu izmaksas būs {} EUR".format(aboli, ievarijums(aboli, cukurs)))
print("Uz",aboli,"kg ābolu izmaksas būs ",ievarijums(aboli, cukurs))