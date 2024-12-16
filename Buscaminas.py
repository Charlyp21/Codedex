import random

mapa = [
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0]
    ]

bombas1 = random.randint(0,8)
bombas2 = random.randint(0,8)

for columna, value in enumerate(mapa):
    for fila, value in enumerate(mapa[columna]):
        if (columna == bombas1 or fila == bombas2) and mapa[columna][fila] == 0:
            mapa[columna].insert((fila+random.randint(-3,+2)), 'x')
            mapa[columna].pop()

for columna, value in enumerate(mapa):
    for fila, value in enumerate(mapa[columna]):
        if mapa[columna][fila] == 'x': 
            mapa[columna][fila+1] = 1
            mapa[columna][fila-1] = 1
for i in range(len(mapa)):
    print(mapa[i])