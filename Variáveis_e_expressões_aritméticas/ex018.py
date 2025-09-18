valor = float(input())

notas_cem = valor//100
valor -= notas_cem * 100
notas_cinquenta = valor//50
valor -= notas_cinquenta * 50
notas_vinte = valor//20
valor -= notas_vinte * 20
notas_dez = valor//10
valor -= notas_dez * 10
notas_cinco = valor//5
valor -= notas_cinco * 5
notas_dois = valor//2
valor -= notas_dois * 2

print(int(notas_cem))
print(int(notas_cinquenta))
print(int(notas_vinte))
print(int(notas_dez))
print(int(notas_cinco))
print(int(notas_dois))
print(int(valor))
