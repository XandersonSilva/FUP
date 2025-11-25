result = []
cont = 0

while True:
    cont += 1
    if cont % 7 != 0 and (cont - 7) % 10 != 0:
        result.append(cont)
    if len(result) == 100:
        break

print(result)