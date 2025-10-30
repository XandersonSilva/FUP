def funcao(x):
    if x < 0:
        return
    else:
        print(x)
        funcao(x-1)


x = int(input(""))
funcao(x)