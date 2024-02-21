# Funktionen herstellen - Erklärungen zu Funktionen

def autoausgabe(anzahl,marke):     # Funktion definieren
    for i in range(0,anzahl): # (anzahl) -> definiert das man unten in der Klammer die anzahl angeben kann und diese nicht beschränkt ist
        print(marke)
        print("=" * len(marke))  # Marke unterstreichen

        #for j in range(0, len(marke)):  # komplizierte / ausführliche variante
        #print("=", end="")

def berecheneDruchschnitt(int_liste):
    summe = 0
    for i in int_liste:     # vorschleife
        summe = summe + i
    durchschnitt = summe / len(int_liste)
    return durchschnitt  # return gibt den Wert zu druchschnitt


# Hauptprogramm
autoausgabe(4,"Peugeot")
print("''''''''''''''''''''''''")
autoausgabe(3,"Mercedes")
print("##############################")

zahlenliste = [7,2,29,45]

durchschnitt = berecheneDruchschnitt(zahlenliste)
print(durchschnitt)