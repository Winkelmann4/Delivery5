# 4 semester exam
# Created Juni 2022 by DK1Gruppe3

# Funktioner bliver importet fra andre Python filer.
from LavProfil import Createprofil
from Sekunde import Seecustomer
from maling import insertmaling

# En funktion bliver oprettet.
def menu():
    # I denne liste ses alle mulighederne som der er i menuen.
    options = ["Opret kunde", "Se kunder", "Opret måling", "Q for quit"]
    for i, option in enumerate(options): # i dette loop kører den hvert objekt i listen.
        # Enumerate tager listen og returnere listen som et optælingsobjekt.
        print("[" + str(i + 1) + "] " + option)

def main(): # En funktion bliver defineret.
    loop = True
    while loop: # while loopet kører indtil et eller flere udsagn ikke er sande/rigtige mere.
        menu() # viser menuen

        try: # Tester koden
            choice = int(input("Main menu")) # Et input som brugeren skal besvare.
            if choice in range(1, 5): # Giver bruger 5 valgmuligheder.
                if choice == 1:
                    Createprofil() # En funktion bliver kørt
                if choice == 2:
                    Seecustomer() # En funktion bliver kørt
                if choice == 3:
                    insertmaling() # En funktion bliver kørt
                if choice == "Q" or "q":
                    break # En kommando for at lukke programmet.
            else:
                quit() # En kommando for at lukke programmet.

        except ValueError:
            print("Forbindelsen er afbrudt, programmet lukkes ned.")
            quit() # En kommando for at lukke programmet.
main()