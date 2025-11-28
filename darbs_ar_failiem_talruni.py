while True:
    vards = input("Vārds: ")
    if vards == "stop":
        break
    else:
        talrunis = input("Talruņa numurs: ")
        d = open("darbs_ar_failiem_talruni.txt","a",encoding="utf-8")
        print(f"{vards}, {talrunis}",file=d)

        