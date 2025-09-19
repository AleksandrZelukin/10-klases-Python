c = input("ievadi, lūdzu kartec numuru: ")
c1 = list(c)
print(c)
print(c1)
if c1[0] =="4":
    print("VISA")
elif c1[0]=="5":
    print("Mastercard")
elif c1[0]=="3":
    print("American Express")

else:
    print("Card NOT valid")
    
    


