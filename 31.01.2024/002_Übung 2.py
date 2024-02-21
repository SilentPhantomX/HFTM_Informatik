# Rechner einfach

print("Dies ist ein einfacher Rechner, folge bitte den Anweisungen")

zahl1 = int(input("Gib eine Zahl ein "))

operator = input("Gib einen Operatior ein aus dieser auswahl +, -, *, / ")

print(operator)

zahl2 = int(input("Gib eine zweite Zahl ein "))

if operator == "+":
    print("Die Lösung ist ", zahl1 + zahl2)
elif operator == "-":
    print("Die Lösung ist ", zahl1 - zahl2)
elif operator == "*":
    print("Die Lösung ist ", zahl1 * zahl2)
elif operator == "/":
    print("Die Lösung ist ", zahl1 / zahl2)

