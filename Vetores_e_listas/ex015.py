vet = []

for i in range(10):
    vet.append(int(input()))

for i in range(10):
    for j in range(i+1, 10):
        if vet[i] == vet[j]:
            print(vet[j])