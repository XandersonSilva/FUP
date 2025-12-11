def function(x):
    result = []
    for i in range(x):
        result.append([])
        for j in range(x):
            result[i].append(0)
    for i in range(x):
        result[i][i] = 1
    return result
