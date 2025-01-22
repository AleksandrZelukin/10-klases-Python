phonebook = dict() #dict

while True:
    vards = input("Vārds: ")
    if vards == "stop":
        break    
    talr = input("Tālrunis: ")
    phonebook[vards] = talr
print(phonebook)
