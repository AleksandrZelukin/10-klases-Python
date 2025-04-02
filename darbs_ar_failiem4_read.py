import csv
# Izveido CSV failu ar datiem un izdrukā to saturu
# Atver failu lasīšanai
with open('datne.csv', 'r', encoding='utf-8') as csvfile:
    # Izveido CSV lasītāju
    csvreader = csv.reader(csvfile, delimiter=',')
    # Izdrukā pirmo rindu (saraksta nosaukumus)

    # Izdrukā katru rindu failā
    for row in csvreader:
        # if row[0] == 'Anna':
            # print(f'{row[0]} {row[1]} {row[2]}')
        # print(row)
        print(f'{row[0]} {row[1]} {row[2]}')

