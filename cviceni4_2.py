def levensteinova_vzdalenost(dotaz1, dotaz2):
    """
    Levensteinova vzdalenost říka, jak jsou 2 řetězce rozdílné, pokud jsou stejné je Levensteinova vzdalenost 0,
    pro řetězce "čas" a "čaj" je Levensteinova vzdalenost 1 (liší se v 1 písmenu)
    """

    delka = max(len(dotaz1), len(dotaz2))
    levenstein = 0
    x = 0
    while x < delka:
        if x < len(dotaz1) and x < len(dotaz2):
            if dotaz1[x] != dotaz2[x]:
                levenstein += 1
        else:
            levenstein += 1
        x += 1
    return levenstein


def levensteinova_vzdalenost_for(dotaz1, dotaz2):

    lenght = min(len(dotaz1), len(dotaz2))
    levenstein = 0
    for x in range(lenght):
        if dotaz1[x] != dotaz2[x]:
            levenstein += 1
    levenstein += abs(len(dotaz1) - len(dotaz2))
    return levenstein


if __name__ == "__main__":

    query1 = "seznam"
    query2 = "seznamka"
    query3 = "sesnam"
    query4 = "seznam"

    print(levensteinova_vzdalenost(query1, query2))
    print(levensteinova_vzdalenost(query2, query3))
    print(levensteinova_vzdalenost(query1, query3))

    print(levensteinova_vzdalenost(query1, query4))


