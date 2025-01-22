'''
== vienāds
!= nav vienāds
> lielāks
< mazāks
<= mazāks vai vienāds
>= lielāks vai vienāds
'''

a = int(input())


if a > 0:
    if a != 10:
        print(a-2)
    else:
        print("pozitivs")
elif a == 0:
    print("Zero!")
else:
    print("negativs")


    
