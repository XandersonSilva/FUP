vet = []
pares = []
cont = 0
for i in range(15):
    inpt = int(input())
    vet.append(inpt)

    if inpt %2 ==0:
        pares.append(inpt)
        cont +=1

print(cont)
for p in pares:
    print(p)