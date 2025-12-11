def funcao(mat, x):
    pos_i = -1
    pos_j = -1
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] == x:
                pos_i = i
                pos_j = j
                return pos_i, pos_j

    return pos_i, pos_j
