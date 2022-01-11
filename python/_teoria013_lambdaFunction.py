def somma_moltiplicazione(x,y):
    somma = x+y
    moltiplicazione = x*y
    return {"somma": somma, "moltiplicazione": moltiplicazione}

#lambda function / permette di fare due operazioni dietro un solo uguale

somma_moltiplicazione2 = lambda x, y : (x+y, x*y)
a = 10
b = 4

s, m = somma_moltiplicazione2(a,b)
print("somma =", s)
print("moltiplicazione =", m)
