def funcao(x):
    num_milhares = x //1000
    novo_numero = x - num_milhares * 1000
    num_centenas = novo_numero //100
    novo_numero -= num_centenas * 100
    num_dezenas = novo_numero//10
    novo_numero -= num_dezenas * 10
    num_unidades =  novo_numero//1

    return num_milhares, num_centenas, num_dezenas, num_unidades
