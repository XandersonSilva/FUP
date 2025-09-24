def verifica_nota(x):
    if x < 0:
        return -1
    if x > 10:
        return -1
    return x

media = 0
erro = 0

for i in range(3):
    num = verifica_nota(float(input()))
    if(num != -1):
        media += num
    else:
        erro = 1
        print("Nota invalida")
        break

if(erro == 0):
    print(f"{(media/3):.2f}")
