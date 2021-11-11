"""
data una lista di parole stampare la parola più lunga
"""

lista = {"ciao", "bellissimo", "migliore"}
lung = 0
for parola in lista:
    if len(parola) > lung:
        lung = len(parola)

print(parola)