def funcao(x):
    horas = x // 3600
    x -= horas * 3600
    minutos = x // 60
    x -= minutos * 60
    segundos = x

    return horas, minutos, segundos
