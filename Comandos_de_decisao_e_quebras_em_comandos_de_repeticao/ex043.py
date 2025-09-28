nome = input()
idade = int(input())

idade_velho = idade
idade_novo  = idade
nome_velho = nome
nome_novo = nome


while True:
    nome = input()
    idade = int(input())
    if idade == -1:
        break
    if idade > idade_velho:
        idade_velho =  idade
        nome_velho = nome
    elif idade_novo > idade:
        idade_novo = idade
        nome_novo = nome

print(nome_novo)
print(idade_novo)
print(nome_velho)
print(idade_velho)
