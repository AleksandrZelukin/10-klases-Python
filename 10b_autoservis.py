import sqlite3

baze = sqlite3.connect("autoservis.db")

cur = baze.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS automobili(
    ID_auto INT Primary key,
    marka text,
    model text,
    gads text,
    krasa text)
    """)

# cur.execute('INSERT INTO automobili VALUES(6,"Opel","Zafira","1999","Black")')
# cur.execute('INSERT INTO automobili VALUES(2,"MAZDA","606","1998","White")')
# cur.execute('INSERT INTO automobili VALUES(3,"Opel","Corsa","2003","Blue")')
# cur.execute('INSERT INTO automobili VALUES(4,"BMW","330i","1999","Black")')
# cur.execute('INSERT INTO automobili VALUES(5,"MB","600","1999","Black")')
# cur.execute('DELETE FROM automobili WHERE ID_auto = 6')
cur.execute('DELETE FROM automobili')
# cur.execute('DROP table automobili')
# ID = int(input())
# m = input()
# mo = input()
# g = input()
# k = input()
# saraksts = (ID,m,mo,g,k)
saraksts = [(6,"Opel","Zafira","1999","Black"),
            (2,"MAZDA","606","1998","White"),
            (4,"BMW","330i","1999","Black")]
#cur.execute('INSERT INTO automobili(ID_auto,marka,model,gads,krasa) VALUES(?,?,?,?,?)',saraksts)
cur.executemany('INSERT INTO automobili(ID_auto,marka,model,gads,krasa) VALUES(?,?,?,?,?)',saraksts)
baze.commit()
baze.close()