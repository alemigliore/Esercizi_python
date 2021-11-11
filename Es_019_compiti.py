"""
Crea un programma in Python in cui inizializzi un dizionario che funga da rubrica telefonica. 
Scegli alcuni dei tuoi amici e usa il loro nome come chiave del dizionario, il loro numero di telefono come valore. 
Stampa il numero di telefono di un amico a tua scelta. Aggiungi un nuovo amico alla rubrica e stampa l’intero dizionario.
"""
rubrica = {"galfre":"3345678398", "elia":"3378965432", "giordan":"3456789456"}
print(rubrica)
nome=input("Dammi il nome: ")
print(rubrica[nome])
nuovo_amico=input("Dammi il nome da aggiungere: ")
nuovo_telefono=input("Dammi il numero: ")
rubrica[nuovo_amico] = nuovo_telefono
print(rubrica)
