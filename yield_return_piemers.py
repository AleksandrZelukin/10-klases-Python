def piemers_one():
    yield "pirmais"
    yield "otrais"
    yield "trešais"	
    
for i in piemers_one():
    print(i)
    
def piemers_duo():
    return "pirmais"
    return "otrais"
    return "trešais"

for i in piemers_duo():
    print(i)	