#Scrivere un programma che data una lista ne stampi una sua permutazione casuale.

import itertools

lista = [3, 2, 1]
listaP = list(itertools.permutations(lista))
print(listaP)