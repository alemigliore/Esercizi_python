"""
Calcola, mediante un opportuno programma in Python, quanti sono i numeri primi minori di 1000. Per stabilire se il 
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

conta=0

for num in range(1000):
    if((ePrimo(num))):
        conta+=1

print(f"Inumeri primi minori di 1000 sono : {conta}") 