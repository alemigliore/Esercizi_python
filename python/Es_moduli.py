import Es_pila_coda as pc  #alias / sinanimo

def main():
    c = pc.Coda()
    p = pc.Pila()
    c1 = pc.Coda()

    risposta = "si"
    counter = 0
    while(risposta == "si"):
        x = int(input("inserisci un numero: "))
        counter += 1
        c.enqueue(x)
        risposta = input("ne vuoi inserire ancora? (si/no)")
    
    c.print()

    for _ in range(counter):
        num = c.denqueue()
        p.push(num)
    
    for _ in range(counter):
        num = p.pop()
        c1.enqueue(num)
    
    c1.print()



if __name__ == "__main__":
    main()
