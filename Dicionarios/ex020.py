def minuscula(char):
    if 'A' <= char <= 'Z':
        return chr(ord(char) + 32)
    return char

def comeca_com(texto, prefixo):
    
    tam_prefixo = 0
    for _ in prefixo:
        tam_prefixo = tam_prefixo + 1
        
    tam_texto = 0
    for _ in texto:
        tam_texto = tam_texto + 1
        
    if tam_prefixo > tam_texto:
        return False
        
    match = True
    for i in range(tam_prefixo):
        char_t = minuscula(texto[i])
        char_p = minuscula(prefixo[i])
        
        if char_t != char_p:
            match = False
            break
            
    return match

def extrair_primeiro_nome(nome_completo):
    primeiro_nome = ""
    for char in nome_completo:
        if char == " ":
            break
        primeiro_nome = primeiro_nome + char
    return primeiro_nome


def inserir_pessoa(lista):
    nome = input("Nome: ")
    email = input("E-mail: ")
    
    rua = input("Rua: ")
    numero = int(input("Numero: "))
    complemento = input("Complemento: ")
    bairro = input("Bairro: ")
    cep = input("CEP: ")
    cidade = input("Cidade: ")
    estado = input("Estado: ")
    pais = input("Pais: ")
    
    endereco = {}
    endereco['rua'] = rua
    endereco['numero'] = numero
    endereco['complemento'] = complemento
    endereco['bairro'] = bairro
    endereco['cep'] = cep
    endereco['cidade'] = cidade
    endereco['estado'] = estado
    endereco['pais'] = pais
    
    ddd = int(input("DDD: "))
    tel_numero = input("Telefone: ")
    
    telefone = {}
    telefone['ddd'] = ddd
    telefone['numero'] = tel_numero
    
    dia_nasc = int(input("Dia do nascimento: "))
    mes_nasc = int(input("Mes do nascimento: "))
    ano_nasc = int(input("Ano do nascimento: "))
    
    nascimento = {}
    nascimento['dia'] = dia_nasc
    nascimento['mes'] = mes_nasc
    nascimento['ano'] = ano_nasc
    
    obs = input("Observacao: ")

    pessoa = {}
    pessoa['nome'] = nome
    pessoa['email'] = email
    pessoa['endereco'] = endereco
    pessoa['telefone'] = telefone
    pessoa['nascimento'] = nascimento
    pessoa['observacao'] = obs

    lista.append(pessoa)

def busca_primeiro_nome(lista, busca):
    resultado = []
    for pessoa in lista:
        primeiro_nome = extrair_primeiro_nome(pessoa['nome'])
        
        if comeca_com(primeiro_nome, busca):
            resultado.append(pessoa)
            
    return resultado

def busca_mes_nascimento(lista, busca):
    resultado = []
    for pessoa in lista:
        if pessoa['nascimento']['mes'] == busca:
            resultado.append(pessoa)
    return resultado

def busca_dia_mes_nascimento(lista, dia_busca, mes_busca):
    resultado = []
    for pessoa in lista:
        if pessoa['nascimento']['dia'] == dia_busca and pessoa['nascimento']['mes'] == mes_busca:
            resultado.append(pessoa)
    return resultado

def agenda_opc(lista, opcao):
    if opcao == 1:
        for pessoa in lista:
            resumo = {}
            resumo['nome'] = pessoa['nome']
            resumo['telefone'] = pessoa['telefone']
            resumo['email'] = pessoa['email']
            print(resumo)
            
    elif opcao == 2:
        for pessoa in lista:
            print(pessoa)
            
    else:
        print("Opcao invalida")


agenda_telefonica = []

while True:
    print("1: Inserir uma pessoa")
    print("2: Buscar por primeiro nome")
    print("3: Buscar por mes de nascimento")
    print("4: Buscar por dia e mes de nascimento")
    print("5: Imprimir agenda")
    print("0: Sair")
    
    i = int(input("Opcao: "))
    
    if i == 0:
        break
        
    elif i == 1:
        inserir_pessoa(agenda_telefonica)
        
    elif i == 2:
        nome_busca = input("Primeiro nome: ")
        encontrados = busca_primeiro_nome(agenda_telefonica, nome_busca)
        for p in encontrados:
            print(p)
            
    elif i == 3:
        mes_busca = int(input("Mes de nascimento: "))
        encontrados = busca_mes_nascimento(agenda_telefonica, mes_busca)
        for p in encontrados:
            print(p)
            
    elif i == 4:
        dia_busca = int(input("Dia do nascimento: "))
        mes_busca = int(input("Mes do nascimento: "))
        encontrados = busca_dia_mes_nascimento(agenda_telefonica, dia_busca, mes_busca)
        for p in encontrados:
            print(p)
            
    elif i == 5:
        print("1: Imprimir apenas nome, telefone e email")
        print("2: Imprimir todos os dados")
        opcao_print = int(input("Opcao: "))
        agenda_opc(agenda_telefonica, opcao_print)
        
    else:
        print("Opcao invalida")