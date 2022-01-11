#Scrivere un programma che data una lista qualsiasi la trasformi in un
#dizionario avente come chiavi gli indici della lista e come valori gli
#elementi.

lista = ["zero", "uno", "due", "tre"]
dict = {}

for k, elemento in enumerate(lista): 
    dict[k] = elemento
print(dict)       

dizionario = {x: elemento for x, elemento in enumerate(lista)}
print(dizionario)