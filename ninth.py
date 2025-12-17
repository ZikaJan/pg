def dec_to_bin(cislo):
    
    cislo = int(cislo)

    if cislo == 0:
        return "0"

    vysledek = ""
    mocniny = [128, 64, 32, 16, 8, 4, 2, 1]

    for x in mocniny:
        if cislo >= x:
            vysledek += "1"
            cislo -= x
        else:
            vysledek += "0"

    return vysledek.lstrip("0")

def test_bin_to_dec():
    assert dec_to_bin("0") == "0"
    assert dec_to_bin(1) == "1"
    assert dec_to_bin("100") == "1100100"
    assert dec_to_bin(101) == "1100101"
    assert dec_to_bin(127) == "1111111"
    assert dec_to_bin("128") == "10000000"