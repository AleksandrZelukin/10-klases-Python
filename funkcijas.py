# def trijsturas_laukums(a,h):
#     s = (a*h)/2
#     print("trijstura laukums: ",s)

x = int(input("Pamats: "))
y = int(input("Augstums: "))
# a = trijsturas_laukums(x,y)

trijsturas_laukums= lambda a,h: (a*h)/2
print("trijstura laukums: ",trijsturas_laukums(x,y))