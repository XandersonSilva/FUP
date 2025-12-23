def multiplicar(mat_aux, texto, linha, coluna, maior, linha_f, coluna_f, x):

    mult_linhas = []
    mult_cols   = []
    diagonal_prnc = 1
    diagonal_segd = 1

    for w in range(len(mat_aux)):
        mult_linhas.append([])
        mult_cols.append([])
        
        # CALCULO DA MULTIPLICACAO DAS LINHAS
        mult_linha = 1

        for n in range(len(mat_aux[w])):
            mult_linha *= mat_aux[w][n]
        mult_linhas[w].append(mult_linha)

        # CALCULO DA MULTIPLICACAO DAS COLUNAS
        mult_col   = 1

        for n in range(len(mat_aux[w])):
            mult_col *= mat_aux[n][w]
        mult_cols[w].append(mult_col)

    # CALCULO DA MULTIPLICACAO DA DIAGONAL PRINCIPAL
    for e in range(len(mat_aux)):
        diagonal_prnc *= mat_aux[e][e]

    
    # CALCULO DA MULTIPLICACAO DA DIAGONAL SEGUNDARIA
    cont_lin = 0
    for e in range(len(mat_aux)-1, -1, -1):
        diagonal_segd *= mat_aux[cont_lin][e]
        cont_lin += 1


    maior_lin = mult_linhas[0][0]
    linha_mt = 0
    for li in range(len(mult_linhas)):
        if maior_lin < mult_linhas[li][0]:
            maior_lin = mult_linhas[li][0]
            linha_mt = li


    maior_col = mult_cols[0][0]
    coluna_mt = 0
    for co in range(len(mult_cols)):
        if maior_col < mult_cols[co][0]:
            maior_col = mult_cols[co][0]
            coluna_mt = co



    if maior_col > maior:
        maior = maior_col
        coluna_f = coluna + coluna_mt
        linha_f = linha
        texto = "baixo"

    if maior_lin > maior:
        maior = maior_lin
        linha_f = linha + linha_mt
        coluna_f = coluna
        texto = "direita"

    if diagonal_prnc > maior:
        maior = diagonal_prnc
        linha_f = linha
        coluna_f = coluna
        texto = "direita baixo"


    if diagonal_segd > maior:
        maior = diagonal_segd
        texto = "esquerda baixo"
        coluna_f = coluna + x - 1
        linha_f = linha

    return maior, texto, linha_f, coluna_f

def funcao(mat, x):
    texto = ''
    linha = 0
    coluna = 0
    linha_f = 0
    coluna_f = 0

    maior = 0
    for linha in range(0, (len(mat)-x) + 1):
        for coluna in range(0, (len(mat)-x) + 1):
            mat_aux = []
            cont = 0
            for k in range(linha, linha+x):
                mat_aux.append([])
                
                for j in range(coluna, (coluna)+x):
                    mat_aux[cont].append(mat[k][j])
                cont +=1
            
            maior, texto, linha_f, coluna_f = multiplicar(
                mat_aux, texto, linha, coluna, maior, linha_f, coluna_f, x
                )
            
            
    return maior, linha_f, coluna_f, texto

