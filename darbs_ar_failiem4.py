import csv
print(dir(csv))
# Izveido CSV failu ar datiem un izdrukā to saturu
# Atver failu lasīšanai
with open('datne.csv', 'r', encoding='utf-8') as csvfile:
    # Izveido CSV lasītāju
    csvreader = csv.reader(csvfile, delimiter=';')

    # Izdrukā katru rindu failā
    for row in csvreader:
        print(row)

saraksts = [{'Vārds': 'Jānis', 'Uzvārds': 'Bērziņš', 'Vecums': 25},
           {'Vārds': 'Anna', 'Uzvārds': 'Kalniņa', 'Vecums': 30},
           {'Vārds': 'Pēteris', 'Uzvārds': 'Ozols', 'Vecums': 28}]
        
# Atver failu rakstīšanai
with open('datne.csv', 'w', encoding='utf-8',newline='') as csvfile:
    # Izveido CSV rakstītāju
    fliednames = ['Vārds', 'Uzvārds', 'Vecums']
    csvwriter = csv.DictWriter(csvfile, fieldnames=fliednames)
    csvwriter.writeheader()
    csvwriter.writerows(saraksts)
