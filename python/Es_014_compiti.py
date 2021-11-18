"""
Scrivi un programma in Python in cui chiedi all’utente un numero e comunichi se esso è primo oppure no. Per stabilire se il 
numero è primo crea una funzione apposita che ritorni True se il numero è primo, False altrimenti. 
"""

def ePrimo(num):
    div,count=2,0

    while div<=num/2 and count==0:
        if num%div==0:
            count+=1
        else:
            div+=1
    if count==0:
       return True 
    else:
       return False

num=int(input("inserisci un numero : "))

if((ePrimo(num))):
    print("E' primo ")
else :
    print("Non è primo")