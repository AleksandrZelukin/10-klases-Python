latv_simbols = {'ā': 'a','č': 'c','ē': 'e','ģ': 'g','ī': 'i','ķ': 'k','ļ': 'l','ņ': 'n','š': 's','ū': 'u','ž': 'z'}
def latv_sinbols(teksts):
    key1 = ""
    key2 = ""
    for i in teksts:
        k = 0
        if i.isupper():
            k += 1
            i = i.lower ()
        if i in latv_simbols:
            k += 2
            i = latv_simbols[i]
        key1 += (i)
        key2 += str(k)
    return key1, key2

vardnica =["vēlēšana","māksla","labs","diena","ka","kā","ka","iet","mīlu","jā","nē","lūdzu","atā","uzredzēšanos"]  

# for i in sorted(vardnica):
#     k1, k2 = latv_sinbols(i)
#     print (i) 
for i in sorted(vardnica):

    print (i)   
    