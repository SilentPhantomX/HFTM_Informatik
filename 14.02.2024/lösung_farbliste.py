# Das Programm gibt aus einer Liste das erste und das letzte Element aus
# Hier werden drei Varianten dafür gezeigt

# Dies ist die fragliche Liste
farbliste = ["Rot","Grün","Weiss","Schwarz"]

# Benutzerinformation
print("Das erste und das letzte Element ausgeben")
print("Basisliste: ", farbliste)

# Dies ist die fragliche Liste
farbliste = ["Rot","Grün","Weiss","Schwarz"]

# 1. Variante: konkatenieren
print(farbliste[0] + " " + farbliste[-1])

# 2. Variante: f-String
print(f"{farbliste[0]} {farbliste[-1]}")

# 3. Variante: C-Like
print("%s %s" % (farbliste[0], farbliste[-1]))