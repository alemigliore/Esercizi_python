#Scrivere un programma che legga una sequenza di caratteri e li stampi in ordine inverso. Usa una pila.

def push(pila,elemento):
    pila.append(elemento)

def pop(pila):
    if(len(pila) != 0):
        return pila.pop()
    else:
        return None

pila,pila1 = [],[]
x = int(input("quanti caratteri vuoi inserire? "))
for k in range(0,x):
    n = int(input("inserisci il numero: "))
    push(pila,n)

print(pila)

#ordine inverso
for k in range(0,x):
    num = pop(pila)
    pila1.append(num)

print(pila1)

