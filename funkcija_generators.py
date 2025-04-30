# https://youtu.be/PrloUblCsFI?si=SNw6SKHkRvaZv9QY
def nedelas(s=0):
    a = ["Pirmdiena","Otrdiena","Trešdiena",
        "Ceturtdiena","Piektdiena",
        "Sestdiena","Svētdiena"]

    while True:
        yield a[s]
        s = (s + 1) % len(a)

aa = input("Ievadi nodēļas dienas numuru (0-6): ")
bb = input("Ievadi nodēļas dienas daudzumu: ")
nedelas_generator = nedelas(int(aa))
for i in range(int(bb)):
    print(next(nedelas_generator))