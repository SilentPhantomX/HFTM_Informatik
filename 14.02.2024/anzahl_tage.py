#Lass den Benutzer zwei Datumswerte im Format dd.mm.yyyy eingeben. 
#Parse die Eingabe, so dass du auf die Elemente (Tag, Monat, Jahr) zugreifen kannst.
#Ermittle die Differenz in Tagen zwischen den beiden Daten. 
#Für diese Übung kannst du aus dem Modul datetime die Klasse date verwenden. 
#Du kannst die Klasse mit dem Befehl

#// from datetime import date //#

#verfügbar machen.

#Über diesen Link findest du mehr Informationen. 
#Orientiere dich auch ein wenig an den Beispielen. 
#Alles was du brauchst, ist dort verpackt.

#Der Programmablauf könnte wie folgt aussehen:

#Anzahl Tage ermitteln
#Startdatum im Format dd.mm.yyyy eingeben: 01.02.2024
#Enddatum im Format dd.mm.yyyy eingeben: 01.03.2024
#Anzahl Tage:  29

import time
from datetime import date

startdatum = input("Startdatum im Format dd.mm.yyyy eingeben: ")
enddatum = input("Enddatum im Format dd.mm.yyyy eingeben: ")
anzahl_tage = abs(startdatum - enddatum)
print("Anzahl Tage: " + anzahl_tage)