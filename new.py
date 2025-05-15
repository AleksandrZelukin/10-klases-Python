a=int(input())
n=list(map(int,input().split(",")))

n2 = [x for x in n if x % 2 == 0 and x > 10]
if n2:
    print(" ".join(map(str, n2)),a)
else:
    print("Nav neviena",a)
