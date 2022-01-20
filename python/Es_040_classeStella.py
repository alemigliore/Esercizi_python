#Creare una classe stella

from random import randint
import turtle

stella=turtle.Turtle()
cielo=turtle.Screen()

class Stella():
    def __init__(self,x,y,n):
        self.x = x
        self.y = y
        self.n = n
    
    def disegna_stella(self):
        stella.speed(1000)
        stella.penup()
        stella.goto(self.x,self.y)
        stella.pendown()

        for _ in range(5):
            stella.forward(100)
            stella.right(144)
    


def main():
    for _ in range(50):        
        s1 = Stella(randint(-400,400),randint(-400,400),5)
        s1.disegna_stella()
    
    cielo.exitonclick()




if __name__ == "__main__":
    main()
