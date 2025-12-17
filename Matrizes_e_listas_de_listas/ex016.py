def mod(n):
    if n >= 0:
        return n
    return -n

def funcao(mat):
    maiores = []
    result = []
    for i in range(len(mat)):
        maior =  mod(mat[i][0])
        for j in range(len(mat[i])):
            if maior < mod(mat[i][j]):
                maior = mod(mat[i][j])
        maiores.append(maior)
        
    for i in range(len(mat)):
        result.append([])
        for j in range(len(mat[i])):
            result[i].append(mat[i][j] / maiores[i])
    return result