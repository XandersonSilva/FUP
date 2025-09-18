numero = int(input())


num_milhares = numero //1000
novo_numero = numero - num_milhares * 1000
num_centenas = novo_numero //100
novo_numero -= num_centenas * 100
num_dezenas = novo_numero//10
novo_numero -= num_dezenas * 10
num_unidades =  novo_numero//1


print(num_milhares)
print(num_centenas)
print(num_dezenas)
print(num_unidades)
