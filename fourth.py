def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):

    typ = figurka["typ"]
    zacatek_r, zacatek_s = figurka["pozice"]
    cil_r, cil_s = cilova_pozice

    if not (1 <= cil_r <= 8 and 1 <= cil_s <= 8):
        return False

    if cilova_pozice in obsazene_pozice:
        return False

    def volna_cesta(zacatek_r, zacatek_s, cil_r, cil_s):
    
        if cil_r > zacatek_r:
            krok_r = 1
        elif cil_r < zacatek_r:
            krok_r = -1
        else:
            krok_r = 0

        if cil_s > zacatek_s:
            krok_s = 1
        elif cil_s < zacatek_s:
            krok_s = -1
        else:
            krok_s = 0
        radek = zacatek_r + krok_r
        sloupec = zacatek_s + krok_s

        while (radek, sloupec) != (cil_r, cil_s):
            if (radek, sloupec) in obsazene_pozice:
                return False
            radek += krok_r
            sloupec += krok_s
        return True

    if typ == "pěšec":
        if cil_s != zacatek_s:
            return False
        if cil_r == zacatek_r + 1 and (cil_r, cil_s) not in obsazene_pozice:
            return True
        if zacatek_r == 1 and cil_r == 3 and (2, zacatek_s) not in obsazene_pozice and (3, zacatek_s) not in obsazene_pozice:
            return True
        return False

    if typ == "jezdec":
        return (abs(cil_r - zacatek_r), abs(cil_s - zacatek_s)) in [(2, 1), (1, 2)]

    if typ == "věž":
        return (zacatek_r == cil_r or zacatek_s == cil_s) and volna_cesta(zacatek_r, zacatek_s, cil_r, cil_s)

    if typ == "střelec":
        return abs(cil_r - zacatek_r) == abs(cil_s - zacatek_s) and volna_cesta(zacatek_r, zacatek_s, cil_r, cil_s)

    if typ == "dáma":
        if (zacatek_r == cil_r or zacatek_s == cil_s) or (abs(cil_r - zacatek_r) == abs(cil_s - zacatek_s)):
            return volna_cesta(zacatek_r, zacatek_s, cil_r, cil_s)
        return False

    if typ == "král":
        return max(abs(cil_r - zacatek_r), abs(cil_s - zacatek_s)) == 1

    return False

if __name__ == "__main__":
    pesec = {"typ": "pěšec", "pozice": (2, 2)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    vez = {"typ": "věž", "pozice": (8, 8)}
    strelec = {"typ": "střelec", "pozice": (6, 3)}
    dama = {"typ": "dáma", "pozice": (8, 3)}
    kral = {"typ": "král", "pozice": (1, 4)}
    obsazene_pozice = {(2, 2), (8, 2), (3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4)}

    print(je_tah_mozny(pesec, (3, 2), obsazene_pozice))  # True
    print(je_tah_mozny(pesec, (4, 2), obsazene_pozice))  # False
    print(je_tah_mozny(pesec, (1, 2), obsazene_pozice))  # False

    print(je_tah_mozny(jezdec, (4, 4), obsazene_pozice))  # False
    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))  # False
    print(je_tah_mozny(jezdec, (1, 2), obsazene_pozice))  # True
    print(je_tah_mozny(jezdec, (9, 3), obsazene_pozice))  # False

    print(je_tah_mozny(dama, (8, 1), obsazene_pozice))  # False
    print(je_tah_mozny(dama, (1, 3), obsazene_pozice))  # False
    print(je_tah_mozny(dama, (3, 8), obsazene_pozice))  # True