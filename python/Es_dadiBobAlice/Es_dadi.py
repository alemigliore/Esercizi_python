# Utilizzando il modulo random (https://docs.python.org/3/library/random.html), simula dieci lanci di un dado per Alice e dieci 
# lanci di un dado per Bob, mediante list comprehension. Il dado è a sei facce. Salva i lanci all’interno di un file, su dieci righe, 
# in cui la prima colonna corrisponde ai lanci di Alice e la seconda a quelli di Bob. Utilizza la virgole come separatore all’interno delle righe.

import random

k = 0

alice = [random.randint(1,6) for _ in range(11)]
bob = [random.randint(1,6) for _ in range(11)]
f = open("./risultatiDadi.txt", "w")
for k in range(11):
    riga = str(f"{alice[k]} , {bob[k]}\n")
    f.write(riga)

f.close()

