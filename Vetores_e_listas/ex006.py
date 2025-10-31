vet = []

for i in range(8):
    vet.append(float(input()))
x = int(input())
y = int(input())

print(f"{(vet[x] + vet[y]):.2f}")
