vet = []
impares = []
cont = 0
for i in range(15):
    inpt = int(input())
    vet.append(inpt)

    if inpt %2 !=0:
        impares.append(inpt)
        cont +=inpt

print(cont)
for p in impares:
    print(p)