estoque = []

for i in range(5):
    codigo = int(input())
    nome = input()
    preco = float(input())
    quantidade = int(input())

    produto = {}
    produto['codigo'] = codigo
    produto['nome'] = nome
    produto['preco'] = preco
    produto['quantidade'] = quantidade

    estoque.append(produto)

while True:
    for prod in estoque:
        print(prod)

    cod_pedido = int(input())

    if cod_pedido == 0:
        break

    qtd_pedido = int(input())

    encontrado = False

    for prod in estoque:
        if prod['codigo'] == cod_pedido:
            encontrado = True
            
            if prod['quantidade'] >= qtd_pedido:
                prod['quantidade'] = prod['quantidade'] - qtd_pedido
            else:
                print("Impossivel atender ao pedido, produto sem estoque suficiente")
            
            break
    
    if not encontrado:
        print("Impossivel atender ao pedido, codigo nao encontrado")
