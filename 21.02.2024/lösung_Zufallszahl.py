import random

zufallszahl = random.randint(1,10)
anzahl_versuche = 0

while True:
    ratezahl = input("Rate die Zahl: ")
    ratezahl_i = int(ratezahl)
    anzahl_versuche = anzahl_versuche +1

    if ratezahl_i == zufallszahl:
       
        break
    elif ratezahl_i > zufallszahl:
        print("Die Zahl ist zu gross")
    else:
        print("Die Zahl ist zu klein")

print("Herzlichen Glückwunsch du hat die Zahl in " + str(anzahl_versuche) " anzahl versuchen erraten")

