x = int(input())

cont = 1
for i in range(1, x+1):
    resultado = ""
    for j in range(0, i):
        resultado += str(cont) + " "
        cont += 1
    print(resultado)
