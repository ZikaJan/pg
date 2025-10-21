def je_prvocislo(cislo):

    if cislo <= 1:
        return False
    
    if cislo == 2:
        return True
    
    if cislo % 2 == 0:
        return False
    
    for n in range(3, int(cislo ** 0.5) + 1, 2):
        if cislo % n == 0:
            return False
    return True

def vrat_prvocisla(maximum):
    maximum = int(maximum)
    seznam = []
    for n in range(2, maximum + 1):
        if je_prvocislo(n):
            seznam.append(n)
    return seznam

if __name__ == "__main__":
    cislo = int(input("Zadej maximum: "))
    prvocisla2 = je_prvocislo(cislo)
    prvocisla = vrat_prvocisla(cislo)
    print(cislo, "->", prvocisla2)
    print(cislo, "->", prvocisla)
    