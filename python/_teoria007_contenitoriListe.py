#le liste sono mutabili

lista = [3,3,1415,"ciao"] #lista eterogenea
print(lista)
numeri_primi = [2,3,5,7,11,13]
print(lista[1:-1]) #indicizzazione con le stesse regole

lista[1] = 2.645
print(lista)

numeri_primi.append(17) #.append aggiunge un oggetto al fondo della lista
print(numeri_primi)
print(f"la lunghezza è {len(numeri_primi)}") #len calcola la lughrzza della lista

altri_numeri_primi = [19,23,29]
molti_numeri_primi = numeri_primi + altri_numeri_primi #+ unisce due liste
print(numeri_primi)
print(altri_numeri_primi)
print(molti_numeri_primi)

print(5*altri_numeri_primi) #scrive n volte gli oggetti nella lista