"""
Un braccio robotico industriale libero di muoversi avanti e indietro lungo una rotaia è impazzito. Ogni secondo si muove scegliendo a caso tra due possibili movimenti: 
1 cm in avanti, oppure 1 cm indietro. Non è possibile togliere corrente al robot senza bloccare tutto lo stabilimento, quindi bisogna attendere lo spegnimento che si 
effettua tutti i fine settimana e oggi purtroppo è lunedì! Il tuo responsabile ti chiede di creare un programma in Python per simulare lo spostamento totale che il 
robot avrà effettuato dopo 5 interi giorni di pazzia.
Definisci una funzione che restituisca uno spostamento casuale (+1 o -1).
Utilizza una list comprehension per creare la  lista contenente tutta la sequenza degli spostamenti casuali.
Infine calcola la somma degli spostamenti casuali per ottenere lo spostamento complessivo accumulato in 5 giorni.

"""

import random

def spostamento():
    spost = random.randint(-1,1)

    return spost


giorni = 5
k = 0
somma = 0
lista = [k for k in range(giorni) if spostamento()]
print(lista)

for j in range(giorni):
    somma = somma + lista[k]

print(f"la somma degli spostamenti e' {somma}")

#CORREZIONE
"""
import random

def spostamentoRandom():
    spostamento=0
    while(spostamento==0):
        spostamento = random.randint(-1,1)#casuale da -1 a 1 caso 0
    
    return spostamento

n=0
listaMovimenti=[spostamentoRandom() for _ in range(432000)]# chiamo la funz spostamento random per il numero di secondi in 5 giorni

sommaMovimenti=0
for movimento in listaMovimenti:
    sommaMovimenti+=listaMovimenti[movimento]#sommo ogni elemento
print(listaMovimenti)
print(f"La somma dei movimenti totali e' : {sommaMovimenti}")

"""
