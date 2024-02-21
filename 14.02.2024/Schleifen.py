# Demo für Schleifen

# print("Gugus")
# print("Gugus")
# print("Gugus")
# print("Gugus")
# print("Gugus")

# Zählschleife (for i in range())
for i in range(0,5):             # range (0,5,2) 0-> von, 5-> bis, 2-> in zweierschritten
    print("Gugus", i)            # i in print zeigt auf welcher durchlauf es ist, muss nicht umbedingt aufgeführt werden

for i in range(20):              # range (20) 20 -> ende, start ist selbstverständlich 0
    print(" Zum Zweiten")

print("Ende")

# Wiederholung mit bedingung (while)
weiter = "j"
while weiter == "j":             # solange die variabel j ist bitte wiederholen
    x = float(input("Gib eine Zahl ein: "))
    print(x * x)
    weiter = input("Nochmal? (J/N) ")

print("Fertig")

# Zählschleife mit while

i = 0
while i < 5:                     
    print("Gugus", i)
    i = i + 1                    # i wird hochgezählt in +1 schritten

# Zählschleife mit einem integrierten Stop

while True:
    x = float(input("Gib eine neue Zahl ein: "))
    print(x * x)
    weiter = input("Nochmal? (J/N) ")
    if weiter == "N":            # es muss N gross zum stopen angegeben werden
        break                    # geht aus der schleife heraus und auch aus der vorschleife

