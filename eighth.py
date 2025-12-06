def bin_to_dec(binarni_cislo):
    cislo = str(binarni_cislo)

    vysledek = 0
    hodnota = 1

    for c in reversed(cislo):
        if c == "1":
            vysledek += hodnota
        hodnota *= 2
    return vysledek

def test_bin_to_dec():
    assert bin_to_dec("0") == 0
    assert bin_to_dec(1) == 1
    assert bin_to_dec("100") == 4
    assert bin_to_dec(101) == 5
    assert bin_to_dec("010101") == 21
    assert bin_to_dec(10000000) == 128