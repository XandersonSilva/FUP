lista_carros = []

for i in range(5):
    modelo = input()
    ano = int(input())
    preco = float(input())

    carro = {}
    carro['modelo'] = modelo
    carro['ano'] = ano
    carro['preco'] = preco

    lista_carros.append(carro)

while True:
    p = float(input())

    if p == 0:
        break

    for carro in lista_carros:
        if carro['preco'] < p:
            print(carro)