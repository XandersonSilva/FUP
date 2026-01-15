carros = []

menor_consumo = 0
menor_consumo_indice = 0
for c in range(5):
    carro = input()
    consumo = float(input())

    dici = {'carro': carro, 'consumo': consumo}
    carros.append(dici)

    if consumo > menor_consumo:
        menor_consumo = consumo
        menor_consumo_indice = c

print(f"Carro mais economico: {carros[menor_consumo_indice]['carro']}")

for c in range(5):
    quilometros = 50 * carros[c]['consumo']
    
    print(f"Carro {carros[c]['carro'] } percorre {quilometros :.2f} kms com 50 litros")

for c in range(5):
    litros = 1000 / carros[c]['consumo']
    
    print(f"Carro {carros[c]['carro'] } precisa de {litros :.2f} litros para percorrer 1000 kms")
