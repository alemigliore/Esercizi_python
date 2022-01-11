# Scrivere un programma che data una lista qualsiasi ne elimini i duplicati.

lista = [0, 2, 1, 4, 5, 1]
listaNuova = []

for k in range (len(lista)-1) :
    j = k+1
    while j < len(lista):
        if lista[k] == lista [j]:
            lista = lista[:j]+ lista[j+1:]
            j -= 1
        j+1



print(lista)
print(listaNuova)
