a = {"Rīga": "Latvija", "Tallinn": "Igaunija",
     "Vilnius": "Lietuva", "Helsinki": "Somija",
     "Daugavpils": "Latvija", "Tartu": "Igaunija", 
     "Kaunas": "Lietuva", "Turku": "Somija"}

while True:
    b = input("Pilsēta: ")
    c = input("valsts: ")
    a[b]=c
    if b == "stop":
        break


for i in a:
    print (i,a[i])
