matriz = [
    ['joao', 8, 7, 6],
    ['pedro', 4.5, 9, 10],
    ['marcos', 6, 6, 8],
]


for linha in matriz:
    for coluna in linha:
        print(str(coluna) + '\t', end = ' ')
    print(' ')