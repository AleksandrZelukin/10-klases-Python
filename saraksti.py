import copy
a = [5,7,9,"Latvija",6.456]

b = copy.deepcopy(a)

print(b)

c = 'Hello!'

d=list(c)
print(c)

if 6 in a:
    print(True)
else: print(False)

