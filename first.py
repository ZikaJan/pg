def sudy_nebo_lichy(hodnota):
    if hodnota % 2:
        print("Číslo" , hodnota, "je liché")
    else:
        print("Číslo" , hodnota, "je sudé")




if __name__ == "__main__":

    cislo = int(input("Zadej cislo: "))
    


sudy_nebo_lichy(cislo)
sudy_nebo_lichy(5)
sudy_nebo_lichy(1000000)




