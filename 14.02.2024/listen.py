# Erklärungenzu Listen

#gemuese1 = "Ruebli"
#gemuese2 = "Brokkoli"
#gemuese3 = "Sellerie"
#gemuese4 = "Federkohl"

#print(gemuese1)
#print(gemuese2)

#gemuese = []     # Leere liste
gemuese = ["Ruebli","Brokkoli","Sellerie","Federkohl"]  # strings in einer Liste
print(gemuese)

print("^°°°°°°°°°°°°°°°^")
# Zugriff über Index
print(gemuese[0])
print(gemuese[1] + "" "" + gemuese[2])
print(len(gemuese))  # Anzahl Elemente ermitteln
print(gemuese[-1])  # letztes Element
#print(gemuese[4])  # geht nicht weil Element nicht exisitert
print("^°°°°°°°°°°°°°°°^")

gemuese.append("Pepperoni") # hinzufügen zur Liste
print(gemuese)
gemuese.append("Frivole Frivole")
print(gemuese)

print("^°°°°°°sesrs°°°°^")
# Einfügen an Position 2
gemuese.insert(2,"Kohlrabi") # Zahl definiert auf welcheposition es kommt
print(gemuese)

print("^°°°°°°°xxx°°°^")
# Entfernen aus der Liste
gemuese.remove("Sellerie")
print(gemuese)

print("^°°°°°°°°°°°dd°°^")
# Letztes Entfernen
print(gemuese.pop()) # Entfernt das letztes Objekt heraus und zeigt es dir
print(gemuese)

print("^xxxxxx°°°°°°°°°°°°^")
# Schleife
for i in range(0,len(gemuese)):   # len = länge der liste
     print(gemuese[i])

print("^°°°°°°°°zu°°°°^")
# g wird definiert und schleife wird ausgeführt
for g in gemuese:
     print(g)

print("^°°°°°°°°°°°°°°°^")
# Positionsbasiertes Löschen
del gemuese[2]

print("^°°°°°°°°°°°°°°°^")
# Liste löschen
#gemuese.clear() # löscht die Liste
#print(len(gemuese))  # die länge der Liste ist 0
#print(gemuese)  # Es wird die leere Liste herausgegeben

print("^°°°°°°°°°°°°°°°^")
# Tupel
# ist eine Liste welche nicht nachverändert werden kann
autos = ("Audi","BMW","Mercedes")
print(autos)

gemuesetupel = tuple(gemuese)
print(gemuesetupel)

gem = "Rüebli, Sellerie, Brokkoli, Federkohl"
gemlist = gem.split(",")
datum = "15.12.2023"
elemente = datum.split(",")
print(elemente)

gem = "Rüebli,\n Sellerie,\n Brokkoli,\n Federkohl"
gemlist = gem.split(",")

print("********************")
print(gemlist)
for i in range(0,len(gemlist)):
     gemlist[i] = gemlist[i].strip()

print(gemlist)
print("==========")
for g in gemlist:
     print(g)