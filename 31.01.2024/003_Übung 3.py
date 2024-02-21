# Rechner, etwas besser

print("Einfacher Taschenrechner. Hallo und willkommen")

zahl1 = int(input("Gib eine Zahl ein "))

if zahl1 == 0:
    print("Auf wiedersehen")
    quit()

operator = input("Gib einen Operatior ein aus dieser auswahl  +,  -,  *,  /,  % ")

zahl2 = int(input("Gib eine zweite Zahl ein "))

if zahl2 == 0:
    print("Auf wiedersehen")
    quit()

if operator == "+":
    print("Die Lösung ist ", zahl1 + zahl2)
elif operator == "-":
    print("Die Lösung ist ", zahl1 - zahl2)
elif operator == "*":
    print("Die Lösung ist ", zahl1 * zahl2)
elif operator == "/":
    print("Die Lösung ist ", zahl1 / zahl2)
elif operator == "%":
    print("Die Lösung ist ", zahl1 % zahl2)
elif operator == 0:
    print("Auf wiedersehen")
    quit()


if operator != "+":
    print("Auf wiedersehen")
    quit()
elif operator != "-":
    print("Auf wiedersehen")
    quit()
elif operator != "*":
    print("Auf wiedersehen")
elif operator != "/":
    print("Auf wiedersehen")
    quit()
elif operator != "%":
    print("Auf wiedersehen")
    quit()