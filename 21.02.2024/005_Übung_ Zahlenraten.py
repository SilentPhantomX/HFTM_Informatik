# Schreibe ein Programm, das es dem Benutzer ermöglich, eine Zahl zwischen 1 und 10 zu erraten. 
# Der Benutzer soll eine Zahl eingeben können, das Programm sagt ihm, ob er die Ratezahl erraten hat, ob er zu tief oder zu hoch war.
# Lass ihn solange Versuche eingeben, bis er die Zahl erraten hat. 
# Zähle die Anzahl Versuche und gib sie am Schluss aus.
# Die Ratezahl kannst du mit dem Zufallsgenerator generieren lassen. Dazu importierst du das Modul random.
# Python-Befehl:
# import random   # Anschliessend kannst du mit dem Aufruf
# ratezahl = random.randint(1,10)  # die Zufallszahl generieren.

import random

zufallszahl = random.randint(1,10)
versuche = 0
# print(zufallszahl)

print("Hallo zum Ratespiel")
print("Welche Zahl zwischen 1 und 10 wird gesucht?")

while True:
    try:
        eingabe_Zufall = int(input("Welches ist die Zuffalszahl? :  "))
        versuche += 1

        if eingabe_Zufall == zufallszahl:
            print(f"Glückwunsch! Du hast die Zahl {zufallszahl} erraten.")
            print(f"Du hast {versuche} Versuche gebraucht.")
            break
        elif eingabe_Zufall < zufallszahl:
            print("Zu niedrig! Versuche es nochmal.")
        else:
            print("Zu hoch! Versuche es nochmal.")
    except ValueError:
        print("Bitte gib eine gültige Zahl ein.")

