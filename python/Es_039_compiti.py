#Scrivere un programma in Python nel quale utilizzando il modulo turtle: - sia presente una 
#funzione che disegni una stella nelle coordinate x e y (passate come parametri alla funzione) 
#- disegni 50 stelle sullo screen posizionate in posizioni casuali.

from random import randint
import turtle

def Stella(x,y,n):
    turtle.hideturtle()
    turtle.speed(1000)
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

    for l in range(n):
        turtle.forward(100)
        turtle.right((360/n*2)%180)
        
x=turtle.Screen()
for _ in range(50):
    Stella(randint(-400,400),randint(-400,400),5)

x.exitonclick()