def funcao(mat):
    somas = []
    for j in range(len(mat[0])):
        soma = 0
        for i in range(len(mat)):
            soma += mat[i][j]
        somas.append(soma)
    return somas
            
