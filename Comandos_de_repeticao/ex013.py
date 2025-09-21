def funcao(x):
    atual = 1
    anterior = 1
    anteanterior = 0
    for i in range(0, x-1):
        atual = anterior + anteanterior
        anteanterior = anterior
        anterior = atual
    return atual

