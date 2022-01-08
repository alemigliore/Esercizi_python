#Scrivere un programma che data una lista qualsiasi la trasformi in un
#dizionario avente come chiavi gli indici della lista e come valori gli
#elementi.

lista = ["zero", "uno", "due", "tre"]
dict = {}

for k in range(len(lista)):
    dict[k] = lista[k]
print(dict)