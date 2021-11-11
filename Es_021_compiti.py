"""
Scrivi un programma in Python che permetta all’utente di inserire le coordinate di due punti del piano cartesiano. 
I punti devono essere salvati all’interno di tuple. Stampa la distanza euclidea tra i due punti.
"""

import math
x=float(input("Inserisci la prima coordinata: "))
y=float(input("Inserisci la seconda coordinata: "))
print("\nSecondo punto")
x2=float(input("Inserisci la prima coordinata: "))
y2=float(input("Inserisci la seconda coordinata: "))
punto1=(x, y)
punto2=(x2, y2)
diffx=punto2[0]-punto1[0]
diffy=punto2[1]-punto1[1]
distanza=((diffx**2)+(diffy**2))**(1/2)
print(distanza)