while True:
    choice = input("Lai turpinatu nospiediet y, lai beigt -n\n")
    if choice =="y":
        print("Cik rezistoru ķedē?")
        count=float(input())

        if count ==2:
            r1=float(input("R1= "))
            r2=float(input("R2= "))
            if r1==0 or r2==0:
                print("Uzmanibu: ISS SAVIENOJUMS!")
            else:    
                r=round(1/(1/r1+1/r2),2)

                print("R =",r,"Ohm")

        if count ==3:
            r1=float(input("R1= "))
            r2=float(input("R2= "))
            r3=float(input("R3= "))

            r=round(1/(1/r1+1/r2+1/r3),2)

            print("R =",r,"Ohm")
    if choice =="n":
        break
        
