#  Data una lista di stringhe estrai da essa la lista di stringhe che sono palindrome e la lista di stringhe che hanno iniziale maiuscola.

def isPalindroma(str):
    if(str == str[::-1]): #se la stringa originale è uguale a quella invertita allora è palindroma 
        return True
    else:
        return False

lista,listaMaiusole,listaPalindrome=["ciao","anna","Pietro","trudy","Ale"],[],[]

for parola in lista:
    if(isPalindroma(parola)):
        listaPalindrome.append(parola)
    
    if(parola[0].isupper()):
        listaMaiusole.append(parola)

print(f"Lista iniziale {lista} , Lista maiuscole  {listaMaiusole} , lista palindromi  {listaPalindrome}")