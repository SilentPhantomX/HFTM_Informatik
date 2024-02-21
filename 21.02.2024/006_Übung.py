# Ausgangslage
# Folgendes Hauptprogramm ist gegeben:

# wahl = menu()
# while wahl != 0:
#     if wahl == 1:
#         eingabe()
#     elif wahl == 2:
#         ausgabe()
#     elif wahl != 0:
#         print("Ungültige Wahl")
#     else:
#         print("Programm wird verlassen")
#     wahl = menu()
# Aufgabe
# Definiere die 3 Funktionen

# menu(): Gibt das Menu aus und lässt den Benutzer eine Wahl treffen. Dies wird ans Hauptprogramm zurückgegeben.

# eingabe(): Lässt den Benutzer beliebig viele Zahlen eingeben. Jede Zahl wird in einer Liste gespeichert. Gibt der Benutzer -1 ein, wird die Eingabe abgebrochen.

# ausgabe(): Gibt die Liste aus. Jedes Element wird ausgegeben und als Trennzeichen wird ein Leerzeichen plus | verwendet.

# Ausgabe
# Folgende Beispielausgabe zeigt eine mögliche Verwendung des Programms:

# 1 - Daten eingeben                        # menue
# 2 - Daten ausgeben                        # menue
# 0 - Programm beenden                      # menue
# ====================

# Ihre Wahl: 1                              # menue
# Gib Ganzzahlen ein (Ende mit -1)          # auswahl
# Zahl? 45                                  # auswahl
# Zahl? 78                                  # auswahl
# Zahl? 21                                  # auswahl
# Zahl? 15                                  # auswahl
# Zahl? 12                                  # auswahl
# Zahl? -1                                  # auswahl
# 1 - Daten eingeben                        # auswahl
# 2 - Daten ausgeben                        # auswahl
# 0 - Programm beenden                      # auswahl
# ====================

# Ihre Wahl: 2
# folgende Daten wurden eingegeben:         # Ausgabe
# 45  | 78  | 21  | 15  | 12  |             # Ausgabe
# 1 - Daten eingeben
# 2 - Daten ausgeben
# 0 - Programm beenden
# ====================

# Ihre Wahl: 1
# Gib Ganzzahlen ein (Ende mit -1)
# Zahl? 16
# Zahl? 18
# Zahl? -1
# 1 - Daten eingeben
# 2 - Daten ausgeben
# 0 - Programm beenden
# ====================

# Ihre Wahl: 2
# folgende Daten wurden eingegeben:
# 45  | 78  | 21  | 15  | 12  | 16  | 18  | 
# 1 - Daten eingeben
# 2 - Daten ausgeben
# 0 - Programm beenden
# ====================

# Ihre Wahl: 0
 
# Tipp:
# Ich würde gleich als allererstes eine leere Liste erzeugen, auf die du sowohl in den Funktionen als auch im Hauptprogramm darauf zugreifen kannst.

def menu():
    print("1 - Daten eingeben")
    print("2 - Daten ausgeben")
    print("0 - Programm beenden")
    print("====================")
    return int(input("\nIhre Wahl: "))
    
def eingabe():
    daten = []
    while True:
        
        zahl = int(input("Zahl? "))
        if zahl == -1:
            break
        daten.append(zahl)
        if ValueError:
            print("Ungültige Eingabe. Bitte geben Sie eine Ganzzahl ein.")
    return daten

def ausgabe(daten):
    print("folgende Daten wurden eingegeben:")
    print(" | " + daten)

#Hauptprogramm  
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
