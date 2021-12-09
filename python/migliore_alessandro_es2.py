"""
Crea un programma Python che disegni una griglia 4 x 4 a maglie quadrate di lato 10, come quella a fianco, 
mediante il modulo turtle. Utilizza il minor numero di righe di codice.
"""

import turtle

griglia = turtle.Turtle()
lati = 4

gradi = (180*(lati-2))/lati
temp = gradi-90
schermo = turtle.getscreen()
for _ in range(16):
    for _ in range(lati):
        griglia.forward(10)
        griglia.left(90-temp)

turtle.exitonclick()

