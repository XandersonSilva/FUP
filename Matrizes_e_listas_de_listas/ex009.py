def funcao(x):
    soma = 0
    for i in range(len(x)):
        for j in range(0, i):
            soma += x[i][j]

    return soma