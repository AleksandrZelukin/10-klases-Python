pirmais = ["Rīga", "Tallinn", "Vilnius"]
otrais = ["Latvia", "Estonia", "Lithuania"]
tresais = [371, 372, 370]

apvienots = list(zip(pirmais, otrais, tresais))
print(apvienots)
# Izvade: [('Rīga', 'Latvia', 371), ('Tallinn', 'Estonia', 372), ('Vilnius', 'Lithuania', 370)]
# # Sarakstu apvienošana izmantojot zip()
# zip() funkcija apvieno vairākus sarakstus, veidojot no tiem tuple elementus.
# Katrs tuple satur vienu elementu no katra sākotnējā saraksta, pamatojoties uz to pozīciju.
# Rezultātā tiek izvelots jauns saraksts, kur katrs elements ir tuple ar atbilstošajiem element
# iem no sākotnējiem sarakstiem.iem.
# Ja saraksti ir dažāda garuma, zip() apstājas pie īsākuma saraksta beigām.
atvienots = list(zip(*apvienots))
print(atvienots)
# Izvade: [('Rīga', 'Tallinn', 'Vilnius'), ('Latvia', 'Estonia', 'Lithuania'), (371, 372, 370)]i no tuple
# Sarakstu atvienošana izmantojot zip() un * operatoru
# Lai atvienotu tuple sarakstu atpakaļ atsevišķos sarakstos, var izmantot zip() kopā ar * operatoru.
# * operators izsaiņo tuple elementus, ļaujot zip() funkcijai tos apstrādāt kā atsevišķus argumentus.
# Rezultātā tiek izveidoti atsevišķi saraksti, kas atbilst sākotnējiem sarakstiem.