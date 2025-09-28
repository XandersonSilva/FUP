def primo(y):
    divisores = 0
    for i in range(1, y+1):
        if y%i == 0:
            divisores += 1
        if divisores > 2:
            return False
    return True

def funcao(x):
    maior = 1
    qcnt = x
    while qcnt != 1:
        for i in range(2, x+1):
            if primo(i):
                if primo(qcnt):
                    if qcnt > maior:
                        maior = qcnt
                    qcnt = qcnt // qcnt
                elif qcnt / i == qcnt // i:
                    qcnt = qcnt // i
                    if i > maior:
                        maior = i
            if qcnt == 1:
                return maior
    return maior
