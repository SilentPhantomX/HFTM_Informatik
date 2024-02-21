# Das Programm fragt den Benutzer nach einer kommagetrennten Liste von Ganzzahlen
# Die Eingabe wird geparst und in eine Liste umgewandelt
# Die Eingabe wird ausserdem in ein Tupel umgewandelt 
# Die Liste und das Tupel wird anschliessend ausgegeben
# Die Anzahl der Elemente in der Liste wird ausgegeben

# Die Ausgabe dient der Benutzerführung
print("Werteliste")

# Der Benutzer wird aufgefordert, ein paar Ganzzahlen einzugeben
eingabe = input("Bitte gib Ganzzahlen mit Komma getrennt ein: ")

# Über das Komma kann der eingegebene String in eine Liste umgewandelt werden
liste = eingabe.split(",")

# Aus einer Liste kann man ein Tupel machen
tupel = tuple(liste)

# Liste ausgeben
print("Liste: ", liste)

# Tupel ausgeben
print("Tupel: ", tupel)

# Die Anzahl Elemente ausgeben
print("Anzahl Elemente: ", len(liste))