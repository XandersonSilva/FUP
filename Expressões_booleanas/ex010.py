def funcao(x1, x2):
    maior = x1
    menor = x2
    if x2 > x1:
        maior = x2
        menor = x1

    MDC = 1
    for i in range(1, maior+1):
        if maior%i == 0 and menor%i == 0:
            MDC = i
    return MDC
