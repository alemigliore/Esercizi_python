#scorrimento alfabeto

def codifica(s,car):
    nuovaStringa = ""
    n = int(input("Inserisci numero di criptazione: "))
    for char in s:
        trova = False
        k=0
        while(trova == False or k>28):
            if char==car[k]:
                trova=True
            else:
                k+=1
        nuovaStringa+=car[(k+n)%28]
    
    print(nuovaStringa)

def decodifica(s,car):
    nuovaStringa = ""
    n = int(input("Inserisci numero di decriptazione: "))
    for char in s:
        trova = False
        k=0
        while(trova == False or k>28):
            if char==car[k]:
                trova=True
            else:
                k+=1
        nuovaStringa+=car[(k-n)%28]
    
    print(nuovaStringa)

caratteri = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"," "]
Cod_dec = input("Vuoi codificare o decodificare [C/D]:")
frase = input("Inserisci la frase: ")
frase = frase.upper()
Cod_dec = Cod_dec.upper()
if Cod_dec == 'C':
    codifica(frase,caratteri)
elif Cod_dec == 'D':
    decodifica(frase,caratteri)
else:
    print("Errore")

"""

lista = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

f = open("./file.txt", "w")

frase = str(input("inserisci una frase: "))
frase_maiuscola = frase.upper()
print(frase_maiuscola)

dec_cod = int(input("inserisci 1 se vuoi codificare e 2 se vuoi decodificare: "))
n = int(input("inseririsci il numero di lettere che vuoi scorrere: "))

if(dec_cod == 1):
    for k in range(len(frase_maiuscola)):
        for j in range(len(lista)):
            if(frase_maiuscola[k] == lista[j]):
                file = lista[j+n]
                f.write(file)
else:
    for k in range(len(frase_maiuscola)):
        for j in range(len(lista)):
            if(frase_maiuscola[k] == lista[j]):
                file = lista[j-n]
                f.write(file)

f.close()
f2 = open("./file.txt", "r")
str_finale = f2.readlines()
x = str_finale[0]
print(x)
f2.close()
"""



            

