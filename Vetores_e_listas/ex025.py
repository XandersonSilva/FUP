def verifica_esta_contido(x,y):
    guardar = True
    for k in range(len(y)):
        if x == y[k]:
            guardar = False
            return guardar
    return guardar
    

def funcao(x,y):
    uniao = []
    for i in range(len(x)):
        if verifica_esta_contido(x[i], uniao):
            uniao.append(x[i])
    for j in range(len(y)):
        if verifica_esta_contido(y[j], uniao):
            uniao.append(y[j])
    return uniao
