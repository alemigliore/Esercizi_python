"""Scrivere una funzione Python ricorsiva che permetta di calcolare il fattoriale di un numero intero."""

def fattoriale(n):
    if n==0:
        return 1
    else:
        return n*fattoriale(n-1)

n = int(input("Inserisci un numero: "))
print(fattoriale(n))