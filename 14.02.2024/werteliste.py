# Werteliste
#Erstelle ein Programm mit dem Namen werteliste.py.
#Das Programm soll den Benutzer um die Eingabe von mehreren Ganzzahlen bitten, die Ganzzahlen sollen mit Komma getrennt werden.
#Die Eingabe soll in den Datentyp Liste umgewandelt werden.
#Die Eingabe soll ausserdem in den Datentyp Tupel umgewandelt werden.
#Anschliesend soll zuerst die Liste und dann das Tupel ausgegeben werden.
#Zum Schluss soll die Anzahl der Elemente, welche eingegeben wurden, ausgegeben werden.
#Der Ablauf könnte etwa wie folgt aussehen:
#Werteliste
#Bitte gib Ganzzahlen mit Komma getrennt ein: 5,8,13,21,34
#Liste:  ['5', '8', '13', '21', '34']
#Tupel:  ('5', '8', '13', '21', '34')
#Anzahl Elemente:  5


print("Werteliste")

werte = input("Bitte gib Ganzzahlen mit Komma grtrennt ein z.B: 5,8,13,21,34 ")
wertelist = werte.split(",")
print(wertelist)

wertetupel = tuple(wertelist)
print(wertetupel)
print("Anzahl Elemente: ", + len(wertelist))