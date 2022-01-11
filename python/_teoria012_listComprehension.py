#list comprehension serve per mettere in una lista tanti valori in una sola riga di codice 


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

k=0

primi = [k for k in range(2,1003) if ePrimo(k)]

print(f"I numeri primi minori di 1000 sono : {primi}") 


#metti in lista i numeri dispari da 1 a 1000


dispari = [k for k in range(1,1000) if (k/2 != 0)] #list comprehension

print(f"I numeri primi minori di 1000 sono : {dispari}") 

#metti in lista i nomi che iniziamo per m

nome = ["marco", "luca", "miglio", "valeria", "mario"]

nomi_m = [nome for nome in nomi if nome[0] = "m"]

print(f"I nomi che iniziano con la lettera M sono : {nomi_m}")