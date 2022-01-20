#incrementa coda

def enqueue(coda,elemento):
    coda.append(elemento)

def denqueue(coda):
    if(len(coda) != 0):
        return coda.pop(0)
    else:
        return None

cliente1 = {"nome":"elia", "id":12345}
cliente2 = {"nome":"alessandro", "id":56789}

coda = []
enqueue(coda, cliente1)
enqueue(coda,cliente2)
print(coda)




