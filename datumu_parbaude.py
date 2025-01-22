from datetime import *

pk = input("PK: ")
pk1 = list(pk)
if pk[7]=="1":
    pk1.insert(4,"19")
elif pk[7]=="2":
    pk1.insert(4,"20")
    
try:
    dd = (''.join(pk1[0:7]))
    dz=datetime.strptime(dd,"%d%m%Y")
    print(dz)
except:
    print("Nepareizi dzimšanas dati.")