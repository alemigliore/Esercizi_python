# Utilizzando le list comprehension scrivi un programma che crei una lista con tutte le potenze di due 
# minori o uguali a un valore inserito dall’utente. Stampa la lista.

x = int(input("inserisci un numero: "))
k = 0

lista = [k for k in range(1,x) if ((k*k) <= x)]
print(f"i numeri con la potenza di due minore o uguale di {x} sono: {lista}")