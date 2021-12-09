# Scrivi un programma in Python che chieda all'utente un numero intero n e disegni, tramite turtle, il poligono regolare a n lati.

import turtle

tar = turtle.Turtle()
lati = int(input("inserisci un numero: "))

gradi = (180*(lati-2))/lati
temp = gradi-90
print(gradi)
schermo = turtle.getscreen()
for _ in range(lati):
    tar.forward(100)
    tar.left(90-temp)

turtle.exitonclick()
