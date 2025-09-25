num = int(input())
maior = num 
menor = num

definido = False

while(num >= 0 ):
    if maior < num:
        maior = num
    if menor > num:
        menor = num
    num = int(input())
    definido = True
    
if definido:
    print(maior)
    print(menor)
