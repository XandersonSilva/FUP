def funcao(x):
    notas_cem = x//100
    x -= notas_cem * 100
    notas_cinquenta = x//50
    x -= notas_cinquenta * 50
    notas_vinte = x//20
    x -= notas_vinte * 20
    notas_dez = x//10
    x -= notas_dez * 10
    notas_cinco = x//5
    x -= notas_cinco * 5
    notas_dois = x//2
    x -= notas_dois * 2
    return notas_cem, notas_cinquenta, notas_vinte, notas_dez, notas_cinco, notas_dois, x
