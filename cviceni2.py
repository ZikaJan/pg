def vrat_treti(seznam2):
    if len(seznam) >= 3:
        return seznam2[2]
    else: 
        return None

def prumer(cislo):
    return sum(cislo) / len(cislo)


if __name__ == "__main__":

    seznam = [12, 50, 1, 3, 5]

    seznam[3] *=3

    seznam.append(69)

    seznam.sort()
    seznam.reverse()

    #print(seznam)
    #print(seznam[3])

    #seznam2 = [1,2,3]
    #print(prumer(seznam))
    #print(prumer(seznam2))
    #treti_prvek = vrat_treti(seznam2)
    #print(treti_prvek)

def naformatuj_text(student):
    #vypocitanecislo = round(prumer(student["znamky"]), 2)
    #vypocitanecislo = prumer(student["znamky"])
    #cislo = round(vypocitanecislo, 2)
    vypocitanecislo = sum(student["znamky"]) / len(student["znamky"])
    cislo = round(vypocitanecislo, 2)
    return f"Student: {student['jmeno']} {student['prijmeni']}, Věk: {student['vek']}, Průměr známek: {cislo}"

if __name__ == "__main__":
    student = {
        "jmeno": "Jan",
        "prijmeni": "Novak",
        "vek": 22,
        "znamky": [1,2,1,3,1,2,1]
        }
    #print(student["prijmeni"])
    #student["vek"] += 1
    #print(student["znamky"][4])

    print(naformatuj_text(student))





