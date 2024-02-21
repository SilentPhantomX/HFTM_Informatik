# Demo Eingaben von Variabeln

# a = input()   # version 1

# print("Ausgabe: " + a)  # version 1

a = input("Gib deinen Namen ein und drücke Enter: ")

print("Ausgabe: " + a)

# ganzzahl = input("Gib eine Ganzzahl ein: ") # variante 2
# print(3 * i_ganzzahl) # variante 2

ganzzahl = input("Gib eine Ganzzahl ein: ")
i_ganzzahl = int(ganzzahl) # umwandlung von sting zu integer
f_ganzzahl = float(ganzzahl) # umwandulg von string zu float
print(type[ganzzahl])
print(type[i_ganzzahl])
print(type[f_ganzzahl])
print(3 * i_ganzzahl)
print(3 * f_ganzzahl)
