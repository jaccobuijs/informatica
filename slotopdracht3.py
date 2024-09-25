
def teken_bord(bord):
   
    print(f"{bord[0]} | {bord[1]} | {bord[2]}")
    print("---------")
    print(f"{bord[3]} | {bord[4]} | {bord[5]}")
    print("---------")
    print(f"{bord[6]} | {bord[7]} | {bord[8]}")

def zet_speler(bord, symbool):
    while True:
        try:
            keuze = int(input(f"Speler {symbool}, kies een vakje (0-8): "))
            
            if 0 <= keuze <= 8:  
                if bord[keuze] == " ":
                    bord[keuze] = symbool
                    break
                else:
                    print("Vakje is al bezet. Kies een ander vakje.")
            else:
                print(" Kies een nummer tussen 0 en 8.")
        except ValueError:
            print("Ongeldige invoer. Voer een geldig getal in.")


def speler_gewonnen(bord, symbool):

    if bord[0] == symbool and bord[1] == symbool and bord[2] == symbool:
        return True
    elif bord[3] == symbool and bord[4] == symbool and bord[5] == symbool:
        return True
    elif bord[6] == symbool and bord[7] == symbool and bord[8] == symbool:
        return True
    elif bord[0] == symbool and bord[3] == symbool and bord[6] == symbool:
        return True
    elif bord[1] == symbool and bord[4] == symbool and bord[7] == symbool:
        return True
    elif bord[2] == symbool and bord[5] == symbool and bord[8] == symbool:
        return True
    elif bord[0] == symbool and bord[4] == symbool and bord[8] == symbool:
        return True
    elif bord[2] == symbool and bord[4] == symbool and bord[6] == symbool:
        return True
    else:
        return False


def speel_boter_kaas_eieren():
    bord = [" "] * 9
    symbool = "X"
    
    for beurt in range(9):
        teken_bord(bord)
        zet_speler(bord, symbool)
        
        if speler_gewonnen(bord, symbool):
            teken_bord(bord)
            print(f"Speler {symbool} heeft gewonnen!")
            return
        
        symbool = "O" if symbool == "X" else "X"
    
    teken_bord(bord)
    print("Het is gelijkspel!")

speel_boter_kaas_eieren()
