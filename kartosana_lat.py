lat={"ā":"a","č":"c","ē":"e","ģ":"g","ī":"i",
     "ķ":"k","ļ":"l","ņ":"n","š":"s","ū":"u","ž":"z"}

def lat_to_kartosana(text):
    key1 = ""
    key2 = ""
    for c in text:
        k=0
        if c.isupper():
            k +=1
            c = c.lower()
        if c in lat:
            k +=2
            c = lat[c]
        key1 += c
        key2 += str(k)
    return key1, key2

aa = ["Zilonis","rīga","vēlēšanas","māksla","ēka",
      "kāds","kā","sāls","auglis","Sala","sals",
      "māja","darbs","kaposti","krējums","mans"]
# for i in sorted(aa, key=lat_to_kartosana):
#     print(i)
    
for i in sorted(aa):
    print(i)