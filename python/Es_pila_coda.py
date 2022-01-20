class Pila():
    #costruttore
    def __init__(self):
        self.pila = [] #self.pila --> attributo interno

    def push(self, elemento):
        self.pila.append(elemento)

    def pop(self):
        if(len(self.pila) != 0):
            return self.pila.pop()
        else:
            return None               

    def print(self):
        for k in range(len(self.pila)):
            print(self.pila[k])

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

def main():
    p1 = Pila()
    p1.push(1)
    p1.push(2)
    p1.print()
    p1.pop()
    p1.print()

    c1 = Coda()
    c1.enqueue("ciao")
    c1.enqueue("ale")
    c1.print()
    c1.denqueue()
    c1.print()

if __name__ == "__main__":
    main()

