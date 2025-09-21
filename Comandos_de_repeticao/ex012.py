def funcao(x1, x2):
    fatorial_x1 = 1
    fatorial_x2 = 1
    fatorial_x1_x2 = 1

    for i in range(x1, 1, -1):
        fatorial_x1 *= i 

    for i in range(x2, 1, -1):
        fatorial_x2 *= i

    for i in range((x1 - x2), 1, -1):
        fatorial_x1_x2 *= i
    
    return fatorial_x1/(fatorial_x2 * fatorial_x1_x2)
