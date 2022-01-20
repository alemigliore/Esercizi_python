"""Scrivere una funzione Python ricorsiva che permetta di stampare i numeri di Fibonacci minori di un valore scelto dall'utente."""

serie = []
def fibonacci(ultimo, penultimo, limite):
    num = ultimo + penultimo
    if num < limite:
        serie.append(num)
        fibonacci(num, ultimo, limite)
    
    return serie

limite = int(input("Inserisci un numero: "))
print(fibonacci(0, 1, limite))