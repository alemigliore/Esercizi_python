#Scrivere un programma in Python che prenda in input il nome file di
#un programma scritto in C. Il programma deve leggere il file e:
#1. Contare il numero di righe totali
#2. Contare il numero di chiamate alla funzione printf
#3. Contare il numero di linee di commento.

def controllaComm(testo):
    commento=0
    for linea in testo:
        for parola in linea.split():
            if parola == "//":
                commento+=1
    
    return commento

f=open("./main.c","r")

testo ,  k = f.readlines()  , 0
nRighe=len(testo)

for linea in testo:
    for parola in linea.split():
        if parola == "printf":
            k+=1

comm = controllaComm(testo)

print(f"Le righe del file sono : {nRighe} , printf è stata chiamata {k} e sono stati inseriti {comm} commenti del codice)")

