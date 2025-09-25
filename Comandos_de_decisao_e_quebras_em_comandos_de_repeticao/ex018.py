def funcao(x):
    dia_num = str(int(x[:2]))
    mes_num = int(x[3:5])
    ano_num = str(int(x[6:]))

    mes = 'dezembro'
    if mes_num == 1:
        mes = 'janeiro'
    elif mes_num == 2:
        mes = 'fevereiro'
    elif mes_num == 3:
        mes = 'marco'
    elif mes_num == 4:
        mes = 'abril'
    elif mes_num == 5:
        mes = 'maio'
    elif mes_num == 6:
        mes = 'junho'
    elif mes_num == 7:
        mes = 'julho'
    elif mes_num == 8:
        mes = 'agosto'
    elif mes_num == 9:
        mes = 'setembro'
    elif mes_num == 10:
        mes = 'outubro'
    elif mes_num == 11:
        mes = 'novembro'
    
    return dia_num + ' de ' + mes + ' de ' + ano_num
