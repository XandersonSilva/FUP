vet = []

for i in range(15):
    vet.append(float(input()))


media = 0
for n in vet:
    media += n
media /= 15

print(f"{media:.2f}")