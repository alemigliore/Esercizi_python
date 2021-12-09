import turtle

f = open("./comandi.txt","w")
snow = turtle.Turtle()
f.write("turtle.Turtle()\n")
finestra = turtle.Screen()
f.write("finestra = turtle.Screen()\n")
riga = 50
f.write("riga = 50\n")
angolo = 15
f.write("angolo = 15\n")
angolo1 = 15
f.write("angolo1 = 15\n")
angolo2 = 30
f.write("angolo2 = 30\n")

for k in range(6):

    snow.goto(0,0)
    snow.right(angolo)
    snow.forward(riga)
    snow.right(angolo1)
    snow.forward(riga)
    snow.right(angolo2)
    snow.forward(riga)
    snow.goto(0,0)

f.write("for k in range(6):\n\n")

f.write("goto:(0,0)\n")
f.write("right:(angolo)\n")
f.write("forward:(riga)\n")
f.write("right:(angolo1)\n")
f.write("forward:(riga)\n")
f.write("right:(angolo2)\n")
f.write("forward:(riga)\n")
f.write("goto:(0,0)\n\n")

riga = 75
f.write("riga = 75\n\n")

for k in range(6):

    snow.goto(0,0)
    snow.right(angolo)
    snow.forward(riga)
    snow.right(angolo1)
    snow.forward(riga)
    snow.right(angolo2)
    snow.forward(riga)
    snow.goto(0,0)

f.write("for k in range(6):\n\n")

f.write("goto:(0,0)\n")
f.write("right:(angolo)\n")
f.write("forward:(riga)\n")
f.write("right:(angolo1)\n")
f.write("forward:(riga)\n")
f.write("right:(angolo2)\n")
f.write("forward:(riga)\n")
f.write("goto:(0,0)\n\n")

riga = 100
f.write("riga = 100\n\n")

for k in range(6):

    snow.goto(0,0)
    snow.right(angolo)
    snow.forward(riga)
    snow.right(angolo1)
    snow.forward(riga)
    snow.right(angolo2)
    snow.forward(riga)
    snow.goto(0,0)

f.write("for k in range(6):\n\n")

f.write("goto:(0,0)\n")
f.write("right:(angolo)\n")
f.write("forward:(riga)\n")
f.write("right:(angolo1)\n")
f.write("forward:(riga)\n")
f.write("right:(angolo2)\n")
f.write("forward:(riga)\n")
f.write("goto:(0,0)\n\n")

finestra.exitonclick()
f.write("finestra.exitonclick()")