def funcao(mat):
    result = []
    for j in range(len(mat[0])):
        result.append([])
        for i in range(len(mat)):
            result[j].append(mat[i][j])
    return result
