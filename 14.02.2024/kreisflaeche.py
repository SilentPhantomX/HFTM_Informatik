# Kreisfläche berechnen
#Erstelle ein Programm mit dem Namen kreisflaeche.py.
#Berechne die Kreisfläche aufgrund des Radius, den du vom Benutzer eingeben lässt.
#Es gibt ein Modul mit dem Namen math. Importiere dieses, damit du auf die Kreiszahl PI über math.pi zugreifen kannst.
#Die Ausführung des Programms könnte so aussehen:
#Kreisfläche berechnen
#Bitte Radius eingeben: 1.5
#Die Kreisfläche beträgt:  7.0685834705770345


import math

print("Kreisfläche berechnen")
zahl1 = float(input("Bitte Radius eingeben: "))

print(zahl1 * zahl1 * math.pi)
