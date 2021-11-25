# Utilizza le list comprehension per generare la tavola pitagorica.

a,b=0,11
lista=[ (a*b) for a in range(11) for b in range (11) ]
print(lista)