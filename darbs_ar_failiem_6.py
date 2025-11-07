aa=input("Ievādi teksts: ")

a = open("darbs_ar_failem_6.txt","a",encoding="utf-8")
print(aa, file=a)

a = open("darbs_ar_failem_6.txt","r",encoding="utf-8")
bb = a.readlines()
for i in bb:
    print(i)

a.close()
