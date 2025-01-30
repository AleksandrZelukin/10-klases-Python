import sqlite3

con = sqlite3.connect("csdd.db")

cur = con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS ipasnieks(
    ID_ipasnieks INT PRIMARY KEY,
    vards text,
    talrunis text)""")

cur.execute("""CREATE TABLE IF NOT EXISTS auto(
    ID_auto TEXT PRIMARY KEY,
    marka text,
    model text,
    gads text,
    ID_ipasnieks INT,
    FOREIGN KEY (ID_ipasnieks) REFERENCES ipasnieks(ID_ipasnieks))""")

i = int(input("Ipašnieka numurs: "))
v = input("Ipašnieka vārds: ")
t = input("Ipašnieka talrunis: ")
print("Aizpidiet automobilus informāciju un pievienojiet īpašnieka numurs")
a = input("Automobila numurs: ")
mar = input("Auto marka: ")
mod = input("Auto modelis: ")
g = input("Auto gads: ")
ia = int(input("Ipašnieka auto: "))
ipasn = (i,v,t)
aut = (a,mar,mod,g,ia)

cur.execute("""INSERT INTO ipasnieks(ID_ipasnieks,vards,talrunis)VALUES(?,?,?)""",ipasn)
cur.execute("""INSERT INTO auto(ID_auto,marka,model,gads,ID_ipasnieks)VALUES(?,?,?,?,?)""",aut)
con.commit()
cur.close()