a = 5
b = 6
c = 12
d = 8

# def pirma_funkcija (x=0,y=6):
#     return x+y
pirma_funkcija = lambda x=0,y=6: x+y
rezultats = pirma_funkcija(a,d)
print(rezultats)