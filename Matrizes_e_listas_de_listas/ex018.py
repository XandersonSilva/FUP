import random

def funcao(x1,x2):
    random.seed(x1)
    mat0 = []
    mat1 = []

    for i in range(x2):
        mat0.append([])
        for j in range(x2):
            mat0[i].append(random.randint(1, 20))

    for i in range(x2):
        mat1.append([])
        for j in range(x2):
            mat1[i].append(mat0[i][j])


    for i in range(1, x2):
        for j in range(i, x2):
            mat1[i-1][j] = 0



    return mat0, mat1