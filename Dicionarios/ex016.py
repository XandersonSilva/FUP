agenda = []

for i in range(5):
    compromisso_texto = input("Descricao: ")
    dia = int(input("Dia: "))
    mes = int(input("Mes: "))
    ano = int(input("Ano: "))

    data = {}
    data['dia'] = dia
    data['mes'] = mes
    data['ano'] = ano

    item_agenda = {}
    item_agenda['compromisso'] = compromisso_texto
    item_agenda['data'] = data

    agenda.append(item_agenda)


while True:
    M = int(input())
    
    if M == 0:
        break
        
    A = int(input())

    compromissos_filtrados = []
    
    for item in agenda:
        if item['data']['mes'] == M and item['data']['ano'] == A:
            compromissos_filtrados.append(item)

    
    tamanho = 0
    for c in compromissos_filtrados:
        tamanho = tamanho + 1
    
    for i in range(tamanho):
        for j in range(tamanho - 1):
            dia_atual = compromissos_filtrados[j]['data']['dia']
            dia_proximo = compromissos_filtrados[j+1]['data']['dia']
            
            if dia_atual > dia_proximo:
                temp = compromissos_filtrados[j]
                compromissos_filtrados[j] = compromissos_filtrados[j+1]
                compromissos_filtrados[j+1] = temp

    for item in compromissos_filtrados:
        print(item)