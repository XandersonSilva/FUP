def fat(x):
    fat = 1
    for i in range(1, x+1):
        fat *= i
    return fat

def funcao(x1, x2):
    soma = 0
    for n in range (x2+1):
        soma += (-1)**n * (x1** (2 * n +1))/fat(2*n+1)
    return soma
