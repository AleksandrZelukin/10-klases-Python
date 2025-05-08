teksts = "abols Ozols abols liepa roze Jolanta"
def vardu_sklais(teksts):
    vardi = teksts.split()
    skaits = {}
    for vards in vardi:
        skaits[vards] = skaits.get(vards, 0) + 1
    return skaits
print(vardu_sklais(teksts))
