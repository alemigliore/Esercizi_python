import turtle

snow = turtle.Turtle()
finestra = turtle.Screen()
f = open("./comandi.txt","r")
righe =  f.readlines()
for riga in righe:
   comando = riga.split(":")
   if(comando[0] == "turtle.turtle()"):
       snow = turtle.turtle()
    elif(comando[0] == "finestra = turtle.Screen()"):
        finestra = turtle.Screen()
    elif(comando[0] == "riga = 50"):
        riga = 50
    elif(comando[0] == "angolo = 15"):
        angolo = 15
    elif(comando[0] == "angolo1 = 15"):
        angolo1 = 15
    elif(comando[0] == "angolo2 = 30"):
        angolo2 = 30
    elif(comando[0] == "for k in range(6):"):
        for k in range(6):
    elif(comando[0] == "goto:(0,0)"):
        go = comando[1].split(",")
        snow.goto(go[0],goto[1][:1])
    elif(comando[0] == "right:(angolo)"):
        snow.right:(angolo)
    elif(comando[0] == "forward:(riga)"):
        snow.forward:(riga)
    elif(comando[0] == "right:(angolo1)"):
        snow.right:(angolo1)
    elif(comando[0] == "right:(angolo2)"):
        snow.right:(angolo2)
    elif(comando[0] == "riga = 75"):
        riga = 75
    elif(comando[0] == "riga = 100"):
        riga = 100
    

f.close()
finestra.exitonclick()