# Demo der Selektion in Python

eingabe = int(input("Gib eine Zahl ein: "))
Name = input("Wie heisst du? ")
print(eingabe)

if eingabe == 4: 
    print("Du gewinnst 50 Fr.")
    print("Herzliche Gratulation")

if eingabe == 6:
    print("Du gewinnst 2Mio.")
    print("Gut gemacht")
else:
    print("Schade, du hast verloren")

if eingabe > 6:
    print("Es gibt nicht mehr als 6 richtige im Lotto")

if True:
    print("Total sinnlos")

print("Programm beendet")

# Zwischen 1 und 6
if eingabe > 0 and eingabe < 7:
    print("Die Eingabe ist zwischen 1 und 6")

# kleiner 5 oder grösser 8
if eingabe < 5 or eingabe > 8:
    print("kleiner 5, grösser 8")


if eingabe == 1:
    print("Dafür gibts kein Geld")
elif eingabe == 2:
    print("Auch dafür gibts nix")
elif eingabe == 3:
    if Name != "Kurt":
        print("Das gibt ca. 10 Fr.")
    else:
        print("Kurts sind die Glücklichen, du bekommst 1Mio.")
elif eingabe == 4:
    print("Das gibt ca. 50 Fr.")
elif eingabe == 5:
    print("Schlappe 100 Fr.")
elif eingabe == 6:
    print("Jetzt gehts in die vollen")
else:
    print("Keine gültige Eingabe")

print


# Vergleichsoperatoren
# ==  Gleichheit
# !=  ungleich
# >   Grösser als
# <   Kleiner als
# >=  Grösser oder gleich
# <=  Kleiner oder gleich


