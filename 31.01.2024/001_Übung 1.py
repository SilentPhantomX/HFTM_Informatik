# Übung 1: Eingaben und Berechnungen

print("Dieses Programm Berechnet die Gesamtkosten für die Familie aus")

name_benutzer = input("Gib deinen Namen ein: ")
print(name_benutzer)

anzahl_kinder = input("Gib nun die anzahl deiner Kinder an:")
print(anzahl_kinder)

anzahl_erwachsene = input("Gib nun die anzahl der Erwachsenen ein inklusive dir: ")
print(anzahl_erwachsene)

i_Kinder = int(anzahl_kinder) # umwandlung von sting zu integer
summe_K = (i_Kinder * 250)

i_Erwachsene = int (anzahl_erwachsene)
summe_E = (i_Erwachsene * 1000)

print("Die Gesamtkosten für deine Familie sind: ",  summe_K + summe_E)
