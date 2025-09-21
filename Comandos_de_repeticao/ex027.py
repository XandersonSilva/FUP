def funcao(x):
    expoente_final = x - 1 
    for i in range(2, x):
        expoente_final **= x - i
    return x** expoente_final
