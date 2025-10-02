
def cislo_mensi_nez_3(hodnota):
    if hodnota > 3:
        print("Číslo" , hodnota, "je větší než 3.")
    elif hodnota < 3:
        print("Číslo" , hodnota, "je menší než 3.")
    else:
        print("Číslo" , hodnota, "je rovna 3.")




if __name__ == "__main__":

    cislo = input("Zadej cislo: ")
    cislo = int(cislo)
    print("Zadane cislo je:", cislo)

cislo_mensi_nez_3(cislo)
cislo_mensi_nez_3(1)






