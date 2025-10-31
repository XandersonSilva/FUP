def funcao(vet):
    n_rep = []
    for i in range(10):
        repete = False
        for j in range(0, 10):
            if i != j and  vet[i] == vet[j]:
                repete = True
        if not repete:
            n_rep.append(vet[i])
    return n_rep
