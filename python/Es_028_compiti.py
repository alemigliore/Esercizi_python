# Utilizza il modulo random per simulare una partita a dadi tra Alice e Bob.

import random

alice = random.randint(1,6)
print("Alice =", alice)
bob = random.randint(1,6)
print("Bob =", bob)

if (alice > bob):
    print("Alice ha vinto")
elif (alice < bob):
    print("Bob ha vinto")
else:
    print("pareggio")