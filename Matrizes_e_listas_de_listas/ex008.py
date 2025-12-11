def funcao(x):
    soma = 0
    for i in range(len(x)):
        ini = i + 1
        for j in range(ini, len(x[i])):
            soma += x[i][j]

    return soma
