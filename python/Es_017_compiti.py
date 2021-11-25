# Creare una lambda function che ritorni True se una stringa inizia con lettera maiuscola, False altrimenti. 

str=input("inserisci una  stringa : ")
controllo = lambda str: (str.isupper())
ok=controllo(str[0])
if(ok == True):
    print("Inizia con una maiuscola ")
else:
    print("Non inizia con una maiuscola ")