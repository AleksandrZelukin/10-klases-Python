# 1. Uzrakstiet programmu, kas pieprasa lietotājam ievadīt skaitļu sarakstu, 
# kas atdalīti ar komatiem.
# 2. Izveidojiet jaunu sarakstu, kurā ir tikai tie skaitļi, 
# kas ir pāra skaitļi un lielāki par 10.
# 3. Ja jaunajā sarakstā ir kādi skaitļi, izvadiet tos,
# pretējā gadījumā izvadiet ziņu "Nav neviena".
n=list(map(int,input().split(",")))
print(n)
# Pirmas variants
n2 = [x for x in n if x % 2 == 0 and x > 10]
if n2:
    print(" ".join(map(str, n2)),a)
else:
    print("Nav neviena",a)
    
    
# Otrais variants
for i in range(len(n)):
    if n[i] % 2 == 0 and n[i] > 10:
        print(n[i], end=" ") 
    else:
        print("Nav neviena", end=" ")
        break   