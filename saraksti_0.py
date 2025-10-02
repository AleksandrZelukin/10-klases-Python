a = ["Rīga", "Tallinn", "Vilnius", "Helsinki"]
b = ["Latvijā", "Igaunijā", "Lietuvā", "Somijā"]
c = ["+371", "+372", "+370", "+358"]

abc = a + b + c
zipped = zip(a, b, c)

for city, country, code in zipped:
    print(f"{city} galvas pilsēta {country}. Valsts kods ir {code}.")