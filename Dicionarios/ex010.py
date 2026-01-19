lista_pessoas = []
for i in range(5):
    nome = input()
    endereco = input()
    telefone = input()
    
    pessoa = {}
    pessoa['nome'] = nome
    pessoa['endereco'] = endereco
    pessoa['telefone'] = telefone
    
    lista_pessoas.append(pessoa)
tamanho = 5
for i in range(tamanho):
    for j in range(tamanho - 1):


        if lista_pessoas[j]['nome'] > lista_pessoas[j+1]['nome']:

            temp = lista_pessoas[j]
            lista_pessoas[j] = lista_pessoas[j+1]
            lista_pessoas[j+1] = temp
for pessoa in lista_pessoas:
    print(pessoa)