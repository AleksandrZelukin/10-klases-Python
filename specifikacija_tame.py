import math

def aprekinat_linoleja_izmaksas(cena_eur_m2, rulla_platums_m, telpas_platums_m, telpas_garums_m):
    """
    Aprēķina linoleja izmaksas telpai.
    Noteikumi:
    1. Telpas izmēri tiek noapaļoti uz augšu līdz veselam metram.
    2. Tiek pieņemts, ka linoleju pērk pēc telpas garuma, ņemot vērā ruļļa platumu.
       Ja telpas platums ir lielāks par ruļļa platumu, būs nepieciešamas vairākas joslas.
    """
    # Noapaļojam telpas izmērus uz augšu
    telpas_platums_noapalots = math.ceil(telpas_platums_m)
    telpas_garums_noapalots = math.ceil(telpas_garums_m)
    
    # Aprēķinām, cik joslas nepieciešamas
    joslu_skaits = math.ceil(telpas_platums_noapalots / rulla_platums_m)
    
    # Kopējais linoleja daudzums kvadrātmetros (joslu skaits * garums * ruļļa platums)
    # Piezīme: Linoleju parasti pārdod pēc tekošajiem metriem no ruļļa.
    # Šeit aprēķinām m2, jo cena dota EUR/m2.
    kopejie_m2 = joslu_skaits * telpas_garums_noapalots * rulla_platums_m
    
    # Izmaksas
    izmaksas = kopejie_m2 * cena_eur_m2
    
    return round(izmaksas, 2)

if __name__ == "__main__":
    # Piemērs
    print("--- Linoleja izmaksu kalkulators ---")
    try:
        cena = float(input("Ievadiet linoleja cenu (EUR/m2): "))
        rulla_platums = float(input("Ievadiet linoleja ruļļa platumu (m): "))
        telpas_platums = float(input("Ievadiet telpas platumu (m): "))
        telpas_garums = float(input("Ievadiet telpas garumu (m): "))
        
        rezultats = aprekinat_linoleja_izmaksas(cena, rulla_platums, telpas_platums, telpas_garums)
        print(f"\nKopējās izmaksas: {rezultats} EUR")
    except ValueError:
        print("\nKļūda: Lūdzu, ievadiet derīgus skaitļus.")
