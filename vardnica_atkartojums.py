a = {}
b = {"Berlīne": "Vācija", 
     "Londona": "Lielbritānija", 
     "Parīze": "Francija", 
     "Roma": "Itālija", 
     "Madride": "Spānija"}
a["Rīga"] = "Latvia"
a["Daugavpils"] = "Latvia"
a["Liepāja"] = "Latvia"
a["Rēzekne"] = "Latvia"
a["Ventspils"] = "Latvia"
a["Talinn"] = "Estonia"
a["Tartu"] = "Estonia"
a["Narva"] = "Estonia"
a["Vilnius"] = "Lithuania"
a["Kaunas"] = "Lithuania"
a["Klaipeda"] = "Lithuania"
a["Panevezys"] = "Lithuania"
a["Šiauliai"] = "Lithuania"

# del a["Rīga"]
# del a["Daugavpils"]
# del a["Liepāja"]

a.update(b)

for i in a:
    print(i, ":", a[i])

print("Kopā Pilsētu skaits vārdnicā: ", len(a))