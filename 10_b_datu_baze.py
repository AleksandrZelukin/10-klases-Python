import sqlite3

datu_baze = sqlite3.connect("mana_datu_baze.db")

cursor = datu_baze.cursor()

cursor.execute("""Create table if not exists auto_ipasnieki(
                pk text primary key,
                vards text, 
                uzvards text, 
                talrunis text)""")

cursor.execute("""create table if not exists automobili(
                valsts_numurs text primary key,
                marka text,
                modelis text,
                gads int,
                ipasnieka_pk text,
                FOREIGN KEY (ipasnieka_pk) REFERENCES auto_ipasnieki(pk)
                ON DELETE CASCADE )""")




cursor.execute("""SELECT * FROM auto_ipasnieki, automobili WHERE ipasnieka_pk = pk""")

cursor.execute('DELETE FROM auto_ipasnieki WHERE vards = "Karlis"')

datu_baze.commit()
datu_baze.close()