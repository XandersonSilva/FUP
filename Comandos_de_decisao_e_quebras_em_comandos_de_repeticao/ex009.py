def menor_maior_meio(x,y,z):
    maior = x
    menor = x
    if maior < y:
        maior = y
    if menor > y:
        menor = y
    if maior < z:
        maior = z
    if menor > z:
        menor = z
    
    if x == maior:
        if y == menor:
            return menor, z, maior
    if x == maior:
        if z == menor:
            return menor, y, maior
    if y == maior:
        if z == menor:
            return menor, x, maior
    if y == maior:
        if x == menor:
            return menor, z, maior
    if z == maior:
        if x == menor:
            return menor, y, maior
    if z == maior:
        if y == menor:
            return menor, x, maior

menor, meio, maior = menor_maior_meio(int(input()), int(input()), int(input()))

print(menor)
print(meio)
print(maior)
