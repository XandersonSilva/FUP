def e_par(x):
    if (x%2)== 0:
        return True
    return False

soma = 0
num = 0
for i in range(4):
    num = int(input())
    if e_par(num):
        soma += num

print(soma)
    