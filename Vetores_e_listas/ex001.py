meses = ['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

def funcao(x):
    data =  x.split("/")
    return  str(int(data[0])) + ' de '+ meses[int(data[1])-1] + ' de ' + data[2]
