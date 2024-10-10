"""
Programma che legge due numeri in input e li moltiplica
solo se sono entrambi positivi.
"""

numero1 = int(input("Inserisci il primo numero: "))
numero2 = int(input("Inserisci il secondo numero: "))

if numero1 > 0 and numero2 > 0:
    risultato = numero1 * numero2
    print(f"Ecco il risultato della moltiplicazione: {risultato}.")
else:
    print("Inserisci entrambi i numeri maggiori di 0.")