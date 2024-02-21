#Auftrag Personenliste:
#Erstelle ein Programm, welches Personennamen über die Tastatur einliest, dies so lange, 
#bis als Name "ende" eingegeben wird (ohne Anführungszeichen). Speichere nach jeder Eingabe den Namen in einer Liste.
#Gib am Schluss die gesamte Liste mit allen Namen aus, wobei jeder Name auf einer eigenen Zeile stehen soll.

namenlist = []

while True:
    namen = input("Gib einen oder mehrere Personennamen ein, falls du fertig bist schreibe ende:")
    for n in namenlist: # jeder auf seiner zeile
        print(n)
    if namen == "ende":
        quit("Die Liste wird geschlossen") 
    elif namen == "":
        continue
    namenlist.append(namen)
    
    print(namenlist)


    



