def funcao(x):
    resultado = 1
    for i in range (1, x+1):
        fatorial = 1
        for j in range(1, i+1):
            fatorial *= j
        resultado += 1/fatorial
    return resultado
