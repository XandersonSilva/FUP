cont = 0
max_num = int(input())
num = float(input())
maior = num
menor = num
if num > maior:
        maior = num
if num < menor:
    menor = num


while cont < max_num-1:
    num = float(input())
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    cont += 1
    
print(f"{menor:.2f}")
print(f"{maior:.2f}")