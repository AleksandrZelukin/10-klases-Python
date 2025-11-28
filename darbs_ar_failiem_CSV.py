import csv

datne = open("darbs_ar_failiem_talruni.txt", encoding="utf-8")
datne_read = csv.reader(datne)

for i in datne_read:
    print(i)