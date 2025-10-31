import random
x = int(input())

random.seed(x)
lst = []
for c in range(12):
    lst.append(random.uniform(-10, 10))

soma = 0.0
negativos = 0
for n in lst:
    if n > 0:
        soma += n
    else:
        negativos += 1

print(negativos)
print(f"{soma:.2f}")