"""
Scrivi un programma in Python che permetta all’utente di inserire due numeri qualsiasi. 
Crea una lista contenente: la somma dei quadrati dei due numeri Il quadrato della somma dei numeri la 
differenza tra i quadrati dei due numeri la differenza tra i numeri al quadrato Stampa la lista ottenuta. 
"""

a = int(input("inserisci un numero: "))
b = int(input("inserisci un numero: "))
somQ = ((a*a)+(b*b))
qSom = ((a + b)**2)
diffQ = ((a*a)-(b*b))
qDiff = ((a - b)**2)
lista = (somQ, qSom, diffQ, qDiff)
print(lista)