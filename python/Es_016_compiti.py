#simula un duello tra giocatori con un dado di 6 facce

import random

miglio = random.randint(1,6)
print("miglio =", miglio)
elia = random.randint(1,6)
print("elia =", elia)

if miglio > elia:
    print("ha vinto miglio")
elif miglio == elia:
    print("è un pareggio")
else:
    print("ha vinto elia")
