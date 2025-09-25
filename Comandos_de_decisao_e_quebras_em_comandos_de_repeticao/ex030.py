rep = int(input())
apareceu = 0

num = int(input())
maior = num
apareceu += 1


for i in range(1, rep):
    num = int(input())
    if num > maior:
        maior = num
        apareceu = 0
    if maior == num:
        apareceu += 1
    
print(maior)
print(apareceu)
    
