from xmlrpc.client import boolean
import Es_pila_coda as pc  #alias / sinanimo

def main():
    c = pc.Coda()

    risposta = "si"
    while(risposta == "si"):
        x = int(input("inserisci un numero: "))
        c.enqueue(x)
        risposta = input("ne vuoi inserire ancora? (si/no)")
    
    c.print()

if __name__ == "__main__":
    main()
