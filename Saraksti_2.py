a = (9,7,5,"Latvija",6.456) # tuple
a = list(a) # pārvēršana par list
a.append(5) #elemetu pievienošana pec kārtas
a.append(7)
a.insert(0,"R") # elementa pievienošana pēc indeksa

print(a)

a.remove(7) # elementa dzēšana
a.pop(0) # elementa noņemšana pēc indeksa

print(a)
# a.clear() # visu elementu dzēšana
print(a)
a=tuple(a) # pārvēršana atpakaļ par tuple
for i in a:
    print(i)