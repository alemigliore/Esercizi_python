"""
Scrivi un programma in Python che permetta all’utente di inserire due numeri qualsiasi. 
Crea una lista contenente: la somma dei quadrati dei due numeri Il quadrato della somma dei numeri la 
differenza tra i quadrati dei due numeri la differenza tra i numeri al quadrato Stampa la lista ottenuta. 
"""

num1= int(input("Dammi il primo numero "))
num2= int(input("Dammi il secondo numero "))
x=[]
x.append(num1**2 + num2**2)
x.append((num1+ num2)**2)
x.append(num1**2 - num2**2)
x.append((num1-num2)**2)
print(x)