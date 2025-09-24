def calcula_raiz(x):
    if x > 0:
        print(f"{x**(1/2):.2f}")
        return
    print("Numero invalido")
    return

num = float(input())
calcula_raiz(num)
