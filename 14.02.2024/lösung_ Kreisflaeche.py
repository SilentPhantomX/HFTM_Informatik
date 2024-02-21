# Programm zur Berechnung einer Kreisfläche
# Die notwendige Formel lautet: r^2 * PI
# Es soll das Modul Math verwendet werden um auf die Konstante PI zuzugreifen
import math

# Die Ausgabe dient der Benutzerführung
print("Kreisfläche berechnen")
# Der Benutzer soll den Radius eingeben. Die Zahl wird als String entgegengenommen
radius = input("Bitte Radius eingeben: ")
# Der String muss in einen float umgewandelt werden, damit Berechnungen gemacht werden können
d_radius = float(radius)
# Nun kann die Fläche berechnet werden
flaeche = d_radius * d_radius * math.pi
# Das Ergebnis soll ausgegeben werden
print("Die Kreisfläche beträgt: ", flaeche)