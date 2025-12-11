def trnsp(mat):
    result = []
    for j in range(len(mat[0])):
        result.append([])
        for i in range(len(mat)):
            result[j].append(mat[i][j])
    return result

def funcao(mat1, mat2):
    trsp = trnsp(mat2)
    rst = []
    for i in range(len(mat1)):
        rst.append([])
        for j in range(len(trsp)):
            mult = 0
            for k in range(len(trsp[j])):
                a = mat1[i][k]
                b = trsp[j][k]
                mult += mat1[i][k] * trsp[j][k]
            rst[i].append(mult)
    return rst
