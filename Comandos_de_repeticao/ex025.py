def funcao(x):
    soma = 0
    for i in range(1, x+1):
        soma += ((i * i) + 1)/(i + 3)
    return soma