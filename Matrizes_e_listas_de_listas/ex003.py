def funcao(x):
    result = []
    for i in range(x):
        result.append([])
        for j in range(x):
            result[i].append(i*j)
    return result
