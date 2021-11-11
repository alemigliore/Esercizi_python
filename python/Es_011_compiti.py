"""
crea un programma che inizializzi la lista x = [0,1,2,3,4,5,6,7,8] e poi
    _crea due nuov liste contenenti ciascuna una delle due metà della lista x.
    _aggiungi il valore 5 alla lista contenente la prima metà
"""
x = [0,1,2,3,4,5,6,7,8]
print(x)
lista1 = (x[:len(x)//2]) #lunghezza lista diviso 2
print(lista1)
lista2 = (x[4:])
print(lista2)
lista1.append(5)
print(lista1)