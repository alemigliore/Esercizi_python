# Creare una lambda function che ritorni True se una stringa è palindroma, False altrimenti. 

isPalindroma=lambda str:(str == str[::-1])
parola=input("inserisci una  stringa : ")
ok=isPalindroma(parola[0])

if(ok == True):
    print("E' palindroma")
else:
    print("Non è palindroma ")