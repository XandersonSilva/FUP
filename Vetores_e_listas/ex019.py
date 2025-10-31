def funcao(x1, x2):
    c = []
    cont = 0
    for i in range(10):
        if i %2 ==0 or i == 0:
            c.append(x1[cont])
        else:
            c.append(x2[cont])
            cont += 1
    return c
