"""
Scrivi un programma che permette all' utente di effettuare le quattro operazioni aritmetiche.
Chiedi all' utente che operazione vuole fare e i due numeri e poi stampa il risultato
"""

operazione = input("Inserisci l' operazione che vuoi effettuere (addizione, sottrazione, moltiplicazione, divisione): ")
num1 = int(input("inserisci il primo numero: "))
num2 = int(input("inserisci il secondo numero: "))

if (operazione == "addizione"):
    risultato = num1 + num2
elif (operazione == "sottrazione"):
    risultato = num1 - num2
elif (operazione == "moltiplicazione"):
    risultato = num1 * num2
else:
    risultato = num1 / num2
print(risultato)