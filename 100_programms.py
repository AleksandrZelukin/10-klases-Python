'''
def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)

x=int(input())
print (fact(x))

values=input()
l=values.split(",")
t=tuple(l)
print (l)
print (t)

items=[x for x in input().split(',')]
items.sort()
print (','.join(items))

lines = []
while True:
    s = input()
    if s:
        lines.append(s.upper())
    else:
        break;

for sentence in lines:
    print (sentence)


'''
