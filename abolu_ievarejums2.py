'''
https://siic-lv.github.io/programmesana/vidusskola/p1/specifikacija/
Specifikacija:
Nepieciešama iespēja definēt recepti un tās sastāvdaļas
Nepieciešama iespēja definēt, cik maksā katra sastāvdaļa
Sistēmai jāaprēķina kopējās ievārījuma izmaksas, balstoties uz ievadīto ābolu apjomu

'''
def izmaksas_receptei(recepte, cena):
    summa = 0
    for sastavdala  in recepte:
        summa += sastavdala * cena[sastavdala]
    return summa


def izmaksas_kopa(abolu_svars):
    recepte = {"cukurs": 0.6, "kanelis": 0.08, "aboli": 2.0, "udens": 0.2}
    cenas = {"cukurs": 0.75, "kanelis": 30.0, "aboli": 0.0, "udens": 0.0}
    izmaksas_kg = izmaksas_receptei(recepte, cenas) / recepte["aboli"]
    return abolu_svars * izmaksas_kg

aboli = izmaksas_kopa(1.5)
print(f"Uz {aboli} kg ābolu izmaksas būs {izmaksas_kopa} EUR")

aboli = 5
# print("Uz {} kg ābolu izmaksas būs {} EUR".format(aboli, izmaksas_kopa(aboli)))

