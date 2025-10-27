def funcao(x1, x2):
    maior = x1
    menor = x2
    if x2 > x1:
        maior = x2
        menor = x1

    MMC = maior
    if x1/x2 == x1//x2:
        return maior
    
    continuar = True
    cont = 1
    while continuar:
        if (menor * cont)/maior == (menor * cont)//maior:
            continuar = False
            return menor * cont
        cont+= 1
