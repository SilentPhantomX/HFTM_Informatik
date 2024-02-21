
liste = []

def menu():
    print("1 - Daten eingeben")
    print("2 - Daten ausgeben")
    print("0 - Programm beenden")
    print("====================")
    print("")
    w = int(input("Ihre Wahl: "))
    return w
    
def eingabe():
    print("Gib Ganzzahlen ein (Ende -1)")
    while True: 
        eingabe = int(input("Zahl? "))
        if eingabe == -1:
            break
        liste.append(eingabe)
        print("")

def ausgabe():
    print("folgende Daten wurden eingegeben:")
    for i in liste:
        print(str(i) + " | ", end="")
        print("")                                   # erste zeilenschaltung
        print("")                                   # Leerzeile

#Hauptprogramm  
if __name__ == '__main__':
    meine_daten = []
    while True:
        wahl = menu()
        if wahl == 1:
            meine_daten.extend(eingabe())
        elif wahl == 2:
            ausgabe(meine_daten)
        elif wahl == 0:
            print("Programm wird verlassen")
            break
        else:
            print("Ungültige Wahl")
