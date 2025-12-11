def funcao(mat):
    tamanho_mat = len(mat)
    soma = 0
    cont = 0
    for i in range(tamanho_mat-1, -1, -1):
        soma += mat[cont][i]
        cont += 1
    return soma
