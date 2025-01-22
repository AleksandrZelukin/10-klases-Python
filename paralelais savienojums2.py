print("aprēķiniet rezistoru paralēlā savienojuma pretestību")
print("Lai turpinātu, nospiediet y, lai beigt - n\n")
while True:
    choice =input()
    if choice == "y":
        
        print("Cik rezistoru ir ķēdē? max=5")
        count=int(input())
        if count == 2:
            r1=float(input("R1="))
            r2=float(input("R2="))
            r=round(1/(1/r1+1/r2),2)
            print("R= ",r,"Ohm")

        if count == 3:
            r1=float(input("R1="))
            r2=float(input("R2="))
            r3=float(input("R3="))
            r=round(1/(1/r1+1/r2+1/r3),2)
            print("R= ",r,"Ohm")


        if count == 4:
            r1=float(input("R1="))
            r2=float(input("R2="))
            r3=float(input("R3="))
            r4=float(input("R4="))
            r=round(1/(1/r1+1/r2+1/r3+1/r4),2)
            print("R= ",r,"Ohm")

        if count == 5:
            r1=float(input("R1="))
            r2=float(input("R2="))
            r3=float(input("R3="))
            r4=float(input("R4="))
            r5=float(input("R5="))
            r=round(1/(1/r1+1/r2+1/r3+1/r4+1/r5),2)
            print("R= ",r,"Ohm")
    
        if count >5:
            print("Rezistoru daudzums pārāk liels!")
        
        if count<2:
            print("Rezistoru daudzums pārāk maz!")

    if choice=="n":
        break
    
