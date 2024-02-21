# Das Programm gibt auf einfachste Art die ersten 20 Zahlen der Fibonacci-Folge aus 
# Die Folge beginnt mit den Zahlen 0 und 1, alle weiteren Zahlen sind jeweils 
# die Summe der zwei vorhergehenden Zahlen. Fülle dazu die Zahlen in eine Liste ab 
# und gibt die Liste am Ende aus. 
wert1 = 0 
wert2 = 1 
liste = [0,1] 
print() 
for i in range(0,18): 
    neuwert = wert1 + wert2 
    liste.append(wert1 + wert2) 
    wert1 = wert2 
    wert2 = neuwert 
    print("Fibonacci ", liste)