liste_1 = [7,3,21,9,15,33]

liste_2 = [9,15,34,7]

schnittmenge =[]

for i in liste_1:
    for j in liste_2:
        if i == j:
            schnittmenge.append(i)

print(schnittmenge)

#Sortieren
for i in range(0,len(schnittmenge)-1):        # sortieren
    for j in range(i +1, len(schnittmenge)):
        if schnittmenge[i] > schnittmenge[j]:      # schaut zwei zahlen an zahl ein grosser als zahl 2
            save = schnittmenge[i]            # sichern
            schnittmenge[i] = schnittmenge[j]      # tauschen
            schnittmenge[j] = save

print(schnittmenge)


