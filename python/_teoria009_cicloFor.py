#ciclo FOR
#esempio 1

print("ESEMPIO 1\n")
numeri_primi = [2,3,5,7,11,13]

print("numeri primi: ")
for numero_primo in numeri_primi: 
    print(numero_primo,end = "-") #,end = "" ---> separa i numeri con ciò compreso tra gli apici (print va a capo in automatico)

print("\n")

#esempio 2

print("ESEMPIO 2\n")
classi = {"4arob", "3arob", "2arob", "4achi", "3ainf"}
indirizzi = {"rob":"smart-robot", "chi":"chimica", "inf":"informatica"}
indice = 0

for classe in classi:
    indice = indice + 1
    indirizzo = indirizzi[classe[-3:]]
    print(f"Posizione {indice} nella lista:")
    print(f"La classe {classe} è dell' indirizzo {indirizzo}",end="\n\n")

#esempio 3


print("ESEMPIO 3\n")
for numero in range(2,23):
    print(numero)