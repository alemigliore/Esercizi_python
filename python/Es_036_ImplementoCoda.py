#implementare una coda

class Coda():
    #costruttore
    def __init__(self):
        self.coda = [] 

    def enqueue(self,elemento):
        self.coda.append(elemento)

    def denqueue(self):
        if(len(self.coda) != 0):
            return self.coda.pop(0)
        else:
            return None               

    def print(self):
        print(self.coda)

c1 = Coda()
c1.enqueue("ciao")
c1.enqueue("ale")
c1.print()
c1.denqueue()
c1.print()