
import math

def somma(a, b):
    return a + b

def sottrazione(a, b):
    return a - b

def moltiplicazione(a, b):
    return a * b

def divisione(a, b):
    if b == 0:
        return "Errore: divisione per zero"
    return a / b

def radice(a):
    if a < 0:
        return "Errore: numero negativo"
    return math.sqrt(a)

print("=== Calcolatrice ===")

while True:
    print("\nOperazioni disponibili:")
    print("1. Somma")
    print("2. Sottrazione")
    print("3. Moltiplicazione")
    print("4. Divisione")
    print("5. Radice quadrata")
    print("6. Esci")

    scelta = input("Scegli un'opzione (1-6): ")

    if scelta == "6":
        print("Uscita dal programma.")
        break

    if scelta == "5":
        numero = float(input("Numero: "))
        print("Risultato:", radice(numero))
    else:
        a = float(input("Numero 1: "))
        b = float(input("Numero 2: "))

        if scelta == "1":
            print("Risultato:", somma(a, b))
        elif scelta == "2":
            print("Risultato:", sottrazione(a, b))
        elif scelta == "3":
            print("Risultato:", moltiplicazione(a, b))
        elif scelta == "4":
            print("Risultato:", divisione(a, b))
        else:
            print("Scelta non valida.")
