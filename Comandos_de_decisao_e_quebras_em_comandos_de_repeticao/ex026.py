cont = 0
num = float(input())
maior = num
menor = num

while cont < 10:
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    if cont == 9:
        cont += 1
        continue
    num = float(input())
    cont += 1
    
print(f"{menor:.2f}")
print(f"{maior:.2f}")