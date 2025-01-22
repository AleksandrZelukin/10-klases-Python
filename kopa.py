a = set() #tukšo kopa izvidošana
a.add(12) 
a.add(27)
a.add(13)
a.update([45,96,72,19,39]) 
b = {"Valmiera", "Rezekne", "Daugavpils", "Ludza"}
c= a.union(b) #divu kopu apvienošana ar metodi union
print(a)
print(c)

b.remove("Valmiera")
b.add("Ogre")
print(b)