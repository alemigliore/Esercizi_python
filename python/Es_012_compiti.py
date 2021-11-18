"""
Crea un programma Python che permetta all'utente di inserire un numero qualunque 
di interi all'interno di una lista. Stampa la lista al termine dell'inserimento. 
"""
risposta = "si"
lista = []
while(risposta == "si"):
    num = int(input("inserisci un numero:"))  
    lista.append(num)
    risposta = input("vuoi continuare ? (si/no): ")

print(lista)