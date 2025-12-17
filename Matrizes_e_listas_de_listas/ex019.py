import random

def funcao(x1,x2,x3,x4,x5):
    random.seed(x3)
    mat0 = []
    rst = []

    for i in range(x1): 
        mat0.append([])
        for j in range(x2):
            mat0[i].append(random.randint(x4, x5))
    
    for i in range(len(mat0)):
        soma = 0
        divisiveis = 0

        for j in range(len(mat0[i])):
            if i % 2 == 0:
                soma += mat0[i][j]
            elif mat0[i][j] % 3 == 0 and mat0[i][j] < 0:
                divisiveis +=1
        if i % 2 == 0:
            rst.append(soma/len(mat0[0]))
        else:
            rst.append(divisiveis)



    return mat0, rst