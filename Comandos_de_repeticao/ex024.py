def fat(x):
    fat = 1
    for i in range(1, x+1):
        fat *= i
    return fat

num =  int(input())
for j in range(num):
    resultado = ''
    for i in range(j+1):
        resultado += str(int(fat(j) / (fat(i) * fat(j - i)))) + ' '
    print(resultado)