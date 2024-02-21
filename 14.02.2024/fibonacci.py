# Erstelle ein Programm mit dem Namen fibonacci.py. Das Programm gibt die ersten 20 Zahlen der Fibonacci-Folge aus. 
# Diese ist wie folgt aufgebaut:Der erste Wert ist eine 0, der zweite Wert eine 1. 
# Alle weiteren Werte berechnen sich jeweils aus der Summe der beiden vorhergehenden Werte.
# 0
# 1
# 1 (=0+1)
# 2 (=1+1)
# 3 (=1+2)
# 5 (=2+3)
# 8 (=3+5)
# 13 (=5+8)
# Die Aufgabe lässt sich mit einer einfachen Zählschleife lösen. Sobald wir Funktionen besprochen haben, 
# kann die Aufgabe erneut mit einer rekursiven Funktion gelöst werden.
# Schreibe die Zahlen in eine Liste und gib am Ende die Liste aus.
# Die Ausgabe könnte wie folgt aussehen:
# Fibonacci  [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]


def fibonacci(n):
    fibonacci_list = [0, 1]  # Die ersten beiden Werte der Fibonacci-Folge
    while len(fibonacci_list) < n:
        next_value = fibonacci_list[-1] + fibonacci_list[-2]
        print(fibonacci_list[-1], "+", fibonacci_list[-2], "=", next_value)
        fibonacci_list.append(next_value)
    
    return fibonacci_list

# Die ersten 20 Fibonacci-Zahlen berechnen
n = 20
fibonacci_sequenc = fibonacci(n)

# Ausgabe der Liste
print("Fibonacci:", fibonacci_sequenc)