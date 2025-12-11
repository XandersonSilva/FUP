def funcao(x):
    
    maior = x[0][0]
    pos_i = 0
    pos_j = 0
    for i in range(len(x)):
        for j in range(len(x[i])):
            if x[i][j] > maior:
                maior = x[i][j]
                pos_i = i
                pos_j = j

    return maior, pos_i, pos_j
