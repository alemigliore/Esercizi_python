# Scrivi un programma in Python che chieda all'utente un numero intero n. Il programma deve creare una lista contente due diverse turtle, 
# orientate in direzioni opposte. Ciascuna turtle disegna poi il poligono regolare a n lati.

import turtle
lista = [turtle.Turtle(),turtle.Turtle()]
lista[1].right(180)
lati = int(input("inserisci il numero dei lati: "))

gradi = (180*(lati-2))/lati
temp = gradi-90
schermo = turtle.getscreen()
for elemento in lista:
    for _ in range(lati):
        elemento.forward(100)
        elemento.left(90-temp)

turtle.exitonclick()