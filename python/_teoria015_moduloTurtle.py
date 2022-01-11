import turtle

snow = turtle.Turtle()
finestra = turtle.Screen()
for k in range(10):
    for i in range(2):
        snow.forward(100)
        snow.right(60)
        snow.forward(100)
        snow.right(120)
    snow.right(50)


finestra.exitonclick()