def funcao(x):
    for i in range(1, x+1):
        resultado = ""
        for k in range(x - i):
            resultado += " "
        for j in range(1, 2*i):
            resultado += "*"
        print(resultado)
