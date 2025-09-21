def funcao(x):
    resultado = 0
    fartorial = 1

    for i in range(x, 1, -1):
        fartorial *= i 
    for i in range(len(str(fartorial)), -1, -1):
        resultado += fartorial//(10 ** i)
        fartorial -= (fartorial//(10 ** i)) * (10 ** i)  
    return resultado
