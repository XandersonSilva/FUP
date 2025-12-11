def funcao(x1, x2):
    result = []
    for i in range(x1):
        result.append([])
        for j in range(x2):
            if i < j:
                result[i].append(((2 * i) + (7 * j)) - 2)
            elif i == j:
                result[i].append((3 * (i**2)) - 1)
            elif i > j:
                result[i].append(((4 * (i**3)) - (5 * (j**2))) + 1)
    
    return result
