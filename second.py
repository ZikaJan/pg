def cislo_text(cislo):
    try:
        nove_cislo = int(cislo)
    except ValueError:
        return "Tvůj vstup není číslo, musíš napsat číslo mezi 0 a 100."

    jednotky = [
         "nula", "jedna", "dva", "tři", "čtyři", "pět", "šest", "sedm", "osm", "devět"
    ]
    desitky = [
        "", "deset", "dvacet", "třicet", "čtyřicet", "padesát", "šedesát", "sedmdesát", "osmdesát", "devadesát"
    ]
    teen = [
        "deset", "jedenáct", "dvanáct", "třináct", "čtrnáct", "patnáct", "šestnáct", "sedmnáct", "osmnáct", "devatenáct"
    ]
    pozice = nove_cislo
    if nove_cislo < 0 or nove_cislo > 100:
        return "mimo rozsah (0–100)"
    
    if nove_cislo < 10:
        return jednotky[pozice]
    
    elif 10 <= nove_cislo < 20:
        return teen[nove_cislo - 10]
    
    elif nove_cislo < 100:
        pozice_d = nove_cislo // 10
        pozice_j = nove_cislo % 10

        if pozice_j == 0:
            return desitky[pozice_d]
        
        else:
            return f"{desitky[pozice_d]} {jednotky[pozice_j]}"
        
    else:
        return "sto"

if __name__ == "__main__":
    cislo = input("Zadej číslo: ")
    text = cislo_text(cislo)
    print(text)