def funcao(x):
    num_centenas = x //100
    novo_numero = x - num_centenas * 100
    num_dezenas = novo_numero//10
    novo_numero -= num_dezenas * 10
    num_unidades =  novo_numero//1

    numero_inverso = (num_unidades * 100) + (num_dezenas * 10) + num_centenas

    return numero_inverso
