# --- FUNÇÕES AUXILIARES DE CÁLCULO ---

def calcular_produto_vetor(lista):
    """Calcula o produto de todos os elementos em uma lista/linha."""
    produto = 1
    for item in lista:
        produto *= item
    return produto

def encontrar_melhor_linha(sub_matriz):
    """Retorna o maior produto entre as linhas e o índice da linha vencedora."""
    maior_p = -1
    indice_vencedor = 0
    for i in range(len(sub_matriz)):
        p_atual = calcular_produto_vetor(sub_matriz[i])
        if i == 0 or p_atual > maior_p:
            maior_p = p_atual
            indice_vencedor = i
    return maior_p, indice_vencedor

def encontrar_melhor_coluna(sub_matriz):
    """Retorna o maior produto entre as colunas e o índice da coluna vencedora."""
    maior_p = -1
    indice_vencedor = 0
    tamanho = len(sub_matriz)
    for j in range(tamanho):
        p_atual = 1
        for i in range(tamanho):
            p_atual *= sub_matriz[i][j]
        
        if j == 0 or p_atual > maior_p:
            maior_p = p_atual
            indice_vencedor = j
    return maior_p, indice_vencedor

def calcular_diagonal_principal(sub_matriz):
    """Retorna o produto da diagonal principal."""
    produto = 1
    for i in range(len(sub_matriz)):
        produto *= sub_matriz[i][i]
    return produto

def calcular_diagonal_secundaria(sub_matriz):
    """Retorna o produto da diagonal secundária."""
    produto = 1
    tamanho = len(sub_matriz)
    for i in range(tamanho):
        produto *= sub_matriz[i][tamanho - 1 - i]
    return produto

# --- LÓGICA DE ATUALIZAÇÃO ---

def atualizar_recorde(valor_novo, texto_novo, lin_nova, col_nova, maior_atual, texto_atual, lin_atual, col_atual):
    """
    Função centralizadora de comparação. 
    Se o novo valor for maior, retorna os novos dados. Caso contrário, mantém os antigos.
    """
    if valor_novo > maior_atual:
        return valor_novo, texto_novo, lin_nova, col_nova
    return maior_atual, texto_atual, lin_atual, col_atual

def processar_multiplicacao(sub_matriz, texto, lin, col, maior, lin_f, col_f, x):
    """
    Orquestra os cálculos da sub-matriz e aplica as atualizações seguindo
    a ordem de prioridade da regra de negócio original.
    """
    # Realiza os cálculos utilizando as funções especialistas
    prod_col, idx_col = encontrar_melhor_coluna(sub_matriz)
    prod_lin, idx_lin = encontrar_melhor_linha(sub_matriz)
    prod_diag_p = calcular_diagonal_principal(sub_matriz)
    prod_diag_s = calcular_diagonal_secundaria(sub_matriz)

    # 1. Coluna (baixo)
    maior, texto, lin_f, col_f = atualizar_recorde(
        prod_col, "baixo", lin, col + idx_col, maior, texto, lin_f, col_f
    )

    # 2. Linha (direita)
    maior, texto, lin_f, col_f = atualizar_recorde(
        prod_lin, "direita", lin + idx_lin, col, maior, texto, lin_f, col_f
    )

    # 3. Diagonal Principal (direita baixo)
    maior, texto, lin_f, col_f = atualizar_recorde(
        prod_diag_p, "direita baixo", lin, col, maior, texto, lin_f, col_f
    )

    # 4. Diagonal Secundária (esquerda baixo)
    maior, texto, lin_f, col_f = atualizar_recorde(
        prod_diag_s, "esquerda baixo", lin, col + x - 1, maior, texto, lin_f, col_f
    )

    return maior, texto, lin_f, col_f

# --- FUNÇÃO PRINCIPAL ---

def funcao(mat, x):
    """Varre a matriz principal buscando a sub-matriz com maior produto."""
    texto = ''
    linha_f = 0
    coluna_f = 0
    maior = 0
    
    limite = (len(mat) - x) + 1

    for i in range(limite):
        for j in range(limite):
            # Extração da sub-matriz
            sub_matriz = []
            for r in range(i, i + x):
                nova_linha = []
                for c in range(j, j + x):
                    nova_linha.append(mat[r][c])
                sub_matriz.append(nova_linha)
            
            # Processamento
            maior, texto, linha_f, coluna_f = processar_multiplicacao(
                sub_matriz, texto, i, j, maior, linha_f, coluna_f, x
            )
            
    return maior, linha_f, coluna_f, texto


def le(m, n):
    mat = []
    for i in range(m):
        mat.append([])
        for j in range(n):
            num = int(input(""))
            mat[i].append(num)
    return mat

mat = le(20, 20)
x = 4
y1, y2, y3, y4 = funcao(mat, x)
print(y1)
print(y2)
print(y3)
print(y4)