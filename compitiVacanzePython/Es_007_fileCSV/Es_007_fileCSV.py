#Il file prezzi.csv (separatore ;) contiene le serie storiche mensili dei
#prezzi di alcuni generi alimentari dal Settembre 2011 a Dicembre
#2016. Immagina una spesa costituita da 5 generi alimentari a tua
#scelta e crea una lista contenente la serie storica del prezzo della tua
#spesa ottenuta sommando i prezzi dei generi alimentari scelti.
#Calcola mese / anno in cui la tua spesa ha costi minimi e massimi.

def data():       
    mese = input("mese: ")
    anno = input("anno: ")
    return mese,anno

def articoli(): 
    lista = []
    for _ in range (5):
        art =  str(input("inseririsci articolo: "))
        lista.append(art)
    return lista


f = open("./prezzi.csv","r")
righe = f.readlines()

riga,colonna = 0,0

mese,anno = data()
listaSpesa = articoli()        


f.close()