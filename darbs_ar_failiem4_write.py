import csv
# Izveido CSV failu ar datiem
saraksts = [{'Vārds': 'Jānis', 'Uzvārds': 'Bērziņš', 'Vecums': 25},
           {'Vārds': 'Anna', 'Uzvārds': 'Kalniņa', 'Vecums': 30},
           {'Vārds': 'Pēteris', 'Uzvārds': 'Ozols', 'Vecums': 28}]
        
# Atver failu rakstīšanai
with open('datne.csv', 'w', encoding='utf-8',newline='') as csvfile:
    # Izveido CSV rakstītāju
    flied_names = ['Vārds', 'Uzvārds', 'Vecums']
    csvwriter = csv.DictWriter(csvfile, fieldnames=flied_names)
    csvwriter.writeheader()
    csvwriter.writerows(saraksts)
