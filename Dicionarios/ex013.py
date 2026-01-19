def eh_digito(n):
    
    if n >= '0' and n <= '9':
        return True
    return False

def processar():
    
    nome = input()
    endereco = input()
    nascimento = input()
    cidade = input()
    cep = input()
    email = input()
    
    tamanho_nasc = 0
    for c in nascimento:
        tamanho_nasc = tamanho_nasc + 1
    
    erro_data = False
    if tamanho_nasc != 10:
        erro_data = True
    elif nascimento[2] != '/' or nascimento[5] != '/':
        erro_data = True
    else:
        
        
        if not eh_digito(nascimento[0]): erro_data = True
        elif not eh_digito(nascimento[1]): erro_data = True
        elif not eh_digito(nascimento[3]): erro_data = True
        elif not eh_digito(nascimento[4]): erro_data = True
        elif not eh_digito(nascimento[6]): erro_data = True
        elif not eh_digito(nascimento[7]): erro_data = True
        elif not eh_digito(nascimento[8]): erro_data = True
        elif not eh_digito(nascimento[9]): erro_data = True
    
    if erro_data:
        print("Data errada")
        return

    
    
    tamanho_cep = 0
    for c in cep:
        tamanho_cep = tamanho_cep + 1
        
    erro_cep = False
    if tamanho_cep != 10:
        erro_cep = True
    elif cep[2] != '.' or cep[6] != '-':
        erro_cep = True
    else:
        
        if not eh_digito(cep[0]): erro_cep = True
        elif not eh_digito(cep[1]): erro_cep = True
        elif not eh_digito(cep[3]): erro_cep = True
        elif not eh_digito(cep[4]): erro_cep = True
        elif not eh_digito(cep[5]): erro_cep = True
        elif not eh_digito(cep[7]): erro_cep = True
        elif not eh_digito(cep[8]): erro_cep = True
        elif not eh_digito(cep[9]): erro_cep = True
        
    if erro_cep:
        print("CEP errado")
        return
    
    tamanho_email = 0
    for c in email:
        tamanho_email = tamanho_email + 1
        
    pos_arroba = -1
    
    
    for i in range(tamanho_email):
        if email[i] == '@':
            pos_arroba = i
            break 
            
    erro_email = False
    
    
    if pos_arroba == -1: 
        erro_email = True
    elif pos_arroba == 0: 
        erro_email = True
    elif pos_arroba == tamanho_email - 1: 
        erro_email = True
    else:
        
        pos_ponto = -1
        
        for i in range(pos_arroba + 1, tamanho_email):
            if email[i] == '.':
                pos_ponto = i
                break 
        
        if pos_ponto == -1: 
            erro_email = True
        elif pos_ponto == pos_arroba + 1: 
            erro_email = True
            
    if erro_email:
        print("E-mail errado")
        return

    
    dados = {}
    dados['nome'] = nome
    dados['endereco'] = endereco
    dados['nascimento'] = nascimento
    dados['cidade'] = cidade
    dados['cep'] = cep
    dados['email'] = email

    print(dados)


processar()