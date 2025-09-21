def funcao(x):
    for i in range(1, x+1):
        resultado = ""
        for j in range(1, i+1):
            resultado += "*"
        print(resultado)
    for i in range(x, 1, -1):
        resultado = ""
        for j in range(i, 1, -1):
            resultado += "*"
        print(resultado)
