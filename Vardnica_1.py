phonebook = dict() #dict
print("""
      Ko vēlies darīt? 
      pievienot ierakstu (1) 
      meklēt ierakstu (2) 
      beigt (3)?""")

if input() == "1":
     print("Ievadi vārdus un telefona numurus")
     while True:
         vards = input("Vārds: ")
         talr = input("Tālrunis: ")
         phonebook[vards] = talr
         print("""
      Ko vēlies darīt? 
      pievienot ierakstu (1) 
      meklēt ierakstu (2) 
      beigt (3)?""")
         if input() == "2":
             break
         if input() == "1":
             continue   
     print(phonebook)

if input() == "2":
    vards = input("Ievadi vārdu, kuru meklēt: ")
    if vards in phonebook:
        print(f"Vārds: {vards}, Tālrunis: {phonebook[vards]}")
    else:
        print("Šis vārds nav atrasts.")
if input() == "3":
    print("Ievadi vārdus un telefona numurus. Lai beigtu, ieraksti 'stop' kā vārdu.")
    while True:
        vards = input("Vārds: ")
        if vards == "stop":
            break
        talr = input("Tālrunis: ")
        phonebook[vards] = talr
    print(phonebook)
