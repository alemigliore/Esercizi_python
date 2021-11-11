"""
Scrivi un programma in Python che permetta all’utente di inserire il suo nome (tramite input) e 
stampi il nome in cui tutti i caratteri tranne il primo sono sostituiti da un *.
"""

name=input("Inserisci il tuo nome: ")
nome2=name[0]+(len(name)-1)* "*"
print(nome2)