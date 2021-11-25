# Genera una lista contenente i quadrati perfetti dispari minori di 1000. 

def ePrimo(num):
    div,k=2,0

    while num/2 >= div and k==0:
        if num%div==0:
            k+=1
        else:
            div+=1
    if k==0:
       return True 
    else:
       return False

lista=[]
for num in range(0,1000):
    if(ePrimo(num) & num%2 != 0):
        lista.append(num)

print(lista)