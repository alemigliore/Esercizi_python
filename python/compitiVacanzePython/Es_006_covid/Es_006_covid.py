#Il file covid-19_gen1.txt contiene la sequenza genomica RNA di un
#virus SARS-COV-2. L&#39;RNA è una sequenza in cui si alternano 4
#simboli (detti nucleotidi): A, T, C, G. L&#39;RNA del virus SARS-COV-2
#contiene 29903 nucleotidi. Leggi covid-19_gen1.txt il file e crea un
#dizionario Python avente come chiavi i nucleotidi A, T, C, G e come
#valori i rispettivi conteggi.

f=open("./covid-19_gen1.txt","r")
testo,dict = f.readlines(),{"A" : 0 ,"T": 0 ,"C": 0 ,"G": 0 }

for line in testo:
        for char in line:
           if char in dict:
               dict[char]+=1

print (dict)