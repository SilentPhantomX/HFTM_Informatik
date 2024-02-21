# In deinem Programm erstellst du die beiden folgenden Listen:
# menge1 = [7,3,21,9,15,33]
# menge2 = [9,15,34,7]
# Erstelle ein Programm, welches aus diesen beiden Listen (Mengen) 
# die Schnittmenge ermittelt und gib diese Schnittmenge aufsteigend geordnet aus,  also:
# Schnittmenge: [7,9,15]

liste_1 = [7,3,21,9,15,33] # strings in einer Liste
print(liste_1)

liste_2 = [9,15,34,7] # strings in einer Liste
print(liste_2)

print("----------------")

liste_1_1 = sorted(liste_1)      # sortierte variante
print(liste_1_1)  

liste_2_1 = sorted(liste_2)      # sortierte variante
print(liste_2_1)

print("----------------")

schnittmenge = []
print(liste_1_1 , liste_2_1)




