a = {"Rīga": "Latvija", "Tallinn": "Igaunija",
     "Vilnius": "Lietuva", "Helsinki": "Somija",
     "Daugavpils": "Latvija", "Tartu": "Igaunija", 
     "Kaunas": "Lietuva", "Turku": "Somija"}

# while True:
#     b = input("Pilsēta: ")
#     c = input("valsts: ")
#     a[b]=c
#     if b == "stop":
#         break

# print("Pilsēta - valsts")

# for i in a:
#     print (i,"-",a[i])
    
print("Pilsēta: ")
pilseta = input()
if pilseta in a:
    print("Valsts:", a[pilseta])
    print("Ievadiet jaunu pilsētu vai 'stop', lai pabeigtu:")
    while True:
        jauna_pilseta = input()
        if jauna_pilseta == "stop":
            break
        if jauna_pilseta in a:
            print("Valsts:", a[jauna_pilseta])
        else:
            print("Šī pilsēta nav datu bāzē.")
            
            