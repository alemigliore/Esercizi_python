"""
l' utente inserisce un numero di interi all' interno di una lista. Stampa la lista al terimine dell inserimento
"""
risposta = "si"
lista = []
while(risposta == "si"):
    num = int(input("inserisci un numero:"))  
    lista.append(num)
    risposta = input("vuoi continuare ? (si/no): ")

print(lista)