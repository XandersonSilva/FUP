cont = 0
soma = 0

while cont < 10:
    num = float(input())
    if num > 0:
        soma += num
        cont += 1
    
print(f"{(soma/10):.2f}")