phonebook = dict() #dictionary
while True:
    print("""Ko daram?
          1 - Pievienot kontaktu
          2 - Meklet kontaktu
          3 - Paradit visus kontaktus
          4 - Dzest kontaktu
          5 - Iziet""")
    choice = input("Ievadi savu izvele: ")
    if choice == "1":
        name = input("Ievadi vardu: ")
        number = input("Ievadi telefona numuru: ")
        phonebook[name] = number
        print(f"Kontakts {name} ar numuru {number} ir pievienots.")
    elif choice == "2":
        name = input("Ievadi vardu, kuru meklet: ")
        if name in phonebook:
            print(f"{name} numurs ir {phonebook[name]}")
        else:
            print(f"{name} nav atrasts telefongrāmatā.")
    elif choice == "3":
        if phonebook:
            print("Visi kontakti:")
            for name, number in phonebook.items():
                print(f"{name}: {number}")
        else:
            print("Telefonbukā nav neviena kontakta.")
    elif choice == "4":
        name = input("Ievadi vardu, kuru dzest: ")
        if name in phonebook:
            del phonebook[name]
            print(f"Kontakts {name} ir dzests.")
        else:
            print(f"Kontakts {name} nav atrasts.")
    elif choice == "5":
        print("Iziet no programmas.")
        break
    else:
        print("Nepareiza izvele, lūdzu mēģiniet vēlreiz.")