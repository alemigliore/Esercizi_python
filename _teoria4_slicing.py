#slicing di stringhe

stringa = "Classe quarta A robotica"
print(f"Il primo carattere della stringa è  {stringa[0]}")
print(f"L' ultimo carattere della stringa è {stringa[0]}")

print(stringa[0:6])
print(stringa[6:2])
print(stringa[:-2])
print(stringa[2:14:2]) #gap - scrive due e ne salt 2
print(stringa[::-1])

#stringa[15]="B" error --> non si possono cambiare le stringhe(IMMUTABILI)
stringa_nuova = stringa[0:14] + "B" + stringa[15:]
print(stringa_nuova)
print(f"LA STRINGA MODIFICATA E' : {stringa_nuova}")