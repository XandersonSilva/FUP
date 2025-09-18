def funcao(x1, x2, x3, x4):
    valor_investido = x1 + x2 + x3

    partes_iguais = x4 / valor_investido

    ganhador_01 = partes_iguais * x1
    ganhador_02 = partes_iguais * x2
    ganhador_03 = partes_iguais * x3
    return ganhador_01, ganhador_02, ganhador_03
