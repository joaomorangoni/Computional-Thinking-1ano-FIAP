matriz = [
    [3,8],
    [1,9],
    [7,4]
]

transposta = [[matriz[l][c] for l in range(len(matriz))] for c in range(len(matriz[0]))]

print(transposta)