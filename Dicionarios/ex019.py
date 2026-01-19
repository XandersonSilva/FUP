cadastro = []

for i in range(5):
    nome = input("Nome: ")
    rua = input("Rua: ")
    bairro = input("Bairro: ")
    cidade = input("Cidade: ")
    estado = input("Estado: ")
    cep = input("CEP: ")
    salario = float(input("Salario: "))
    identidade = input("Identidade: ")
    cpf = input("CPF: ")
    civil = input("Estado Civil: ")
    telefone = input("Telefone: ")
    idade = int(input("Idade: "))
    sexo = input("Sexo: ")

    endereco = {}
    endereco['rua'] = rua
    endereco['bairro'] = bairro
    endereco['cidade'] = cidade
    endereco['estado'] = estado
    endereco['cep'] = cep

    pessoa = {}
    pessoa['nome'] = nome
    pessoa['endereco'] = endereco
    pessoa['salario'] = salario
    pessoa['identidade'] = identidade
    pessoa['cpf'] = cpf
    pessoa['civil'] = civil
    pessoa['telefone'] = telefone
    pessoa['idade'] = idade
    pessoa['sexo'] = sexo

    cadastro.append(pessoa)


print("Pessoa com maior idade:")
pessoa_maior_idade = cadastro[0]
for p in cadastro:
    if p['idade'] > pessoa_maior_idade['idade']:
        pessoa_maior_idade = p
print(pessoa_maior_idade)

print("Pessoas do sexo masculino:")
for p in cadastro:
    if p['sexo'] == 'Masculino':
        print(p)

print("Pessoas com salario maior que 1000:")
for p in cadastro:
    if p['salario'] > 1000:
        print(p)

id_busca = input("Identidade: ")
for p in cadastro:
    if p['identidade'] == id_busca:
        print(p)