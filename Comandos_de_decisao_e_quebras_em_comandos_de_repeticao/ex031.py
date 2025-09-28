x01 = int(input())
x02 = int(input())

ini = x01
fim = x02 + 1

if x01 > x02:
    ini = x02
    fim = x01 + 1

somatorio = 0
produto = 1

for i in range(ini, fim):
    if i%2 == 0:
        somatorio += i
    else:
        produto *= i

print(somatorio)
print(produto)