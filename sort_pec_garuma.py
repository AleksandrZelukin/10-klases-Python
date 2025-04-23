a=["mion","abba","abracadabra","baba","zoro"]
a.sort()
def sort_pec_garuma(a):
    return len(a) #lenght of string
a.sort(key=sort_pec_garuma, reverse=True)
print(a)