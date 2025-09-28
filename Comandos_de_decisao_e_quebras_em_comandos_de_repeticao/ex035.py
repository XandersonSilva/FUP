for i in range(1000, 10000):
    aux = i
    milhar = aux // 1000
    aux = aux - (milhar * 1000)
    centena = aux // 100
    aux = aux - (centena * 100)

    milhar_centena = (milhar * 10) + centena
    dezena_unidade = aux

    soma_das_partes = milhar_centena + dezena_unidade

    if soma_das_partes ** 2 == i:
        print(i)