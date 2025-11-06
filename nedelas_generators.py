def nedelas_generators(s=0):  
    aa = ["Pirmdiena", "Otrdiena", "Trešdiena", "Ceturtdiena", "Piektdiena", "Sestdiena", "Svētdiena"]
    while True:
        yield aa[s]
        s = (s + 1) % 7
        
generator = nedelas_generators(2)  # Starting from "Trešdiena"
for _ in range(14):
    print(next(generator))