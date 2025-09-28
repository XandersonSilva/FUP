def funcao(x1, x2):
    # Retorna Falso para quando as strings tem tamanho diferente tomando como
    # axioma que se elas têm tamanho diferente elas são diferentes. (a questão
    # não informa para ignorar espaços extras na string e analisar somente o conteúdo)
    if len(x1) != len(x2):
        return False
    for i in range(len(x1)):
        if x1[i] != x2[i]:
            return False
    return True
