a = int(input("Ievadi a: "))
b = int(input("Ievadi b: "))
c = int(input("Ievadi c: "))
if a >= b and a >= c and b >= c:
    print(a, b, c)
elif b >= c and b >= a and c >= a:
    print(b, c, a)
elif c >= a and c >= b and a >= b:
    print(c, a, b) 