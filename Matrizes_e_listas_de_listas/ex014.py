




def funcao(mat1, mat2):
    result = []
    for i in range(len(mat1)):
        result.append([])
        for j in range(len(mat1[i])):
            result[i].append(mat1[i][j]+mat2[i][j])
    return result

