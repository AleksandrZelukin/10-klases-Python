atlikums = int(input("ievadiet atlikumu summu: "))

kassa = (50,20,10,5,2,1)

a = atlikums//50
b = (atlikums-a*50)//20
c = (atlikums-a*50-b*20)//10
d = (atlikums-a*50-b*20-c*10)//5
e = (atlikums-a*50-b*20-c*10-d*5)//2
f = (atlikums-a*50-b*20-c*10-d*5-e*2)//1

print(f"""Lai izdot atlikumu {atlikums} centu, nepiecešams 
      {a} monetas pa {kassa[0]}, 
      {b} monetas pa {kassa[1]}, 
      {c} monetas pa {kassa[2]}, 
      {d} monetas pa {kassa[3]},
      {e} monetas pa {kassa[4]} un 
      {f} monetas pa {kassa[5]} centu""")

    # Function to calculate the number of coins needed for each denomination
def calculate_coins(atlikums, kassa):
        result = []
        for coin in kassa:
            num_coins = atlikums // coin
            result.append(num_coins)
            atlikums -= num_coins * coin
        return result

    # Input for custom denominations
custom_kassa = input("Ievadiet monētu nominālus, atdalot tos ar komatiem (piemēram, 50,20,10,5,2,1): ")
kassa = tuple(map(int, custom_kassa.split(',')))

    # Calculate the number of coins for each denomination
coins = calculate_coins(atlikums, kassa)

    # Print the result
print(f"Lai izdot atlikumu {atlikums} centu, nepieciešams:")
for i, coin in enumerate(kassa):
        print(f"{coins[i]} monetas pa {coin} centu")

