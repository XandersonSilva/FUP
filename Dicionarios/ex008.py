import math

def converter(ponto_polar):

    r = ponto_polar['r']
    a = ponto_polar['a']


    x = r * math.cos(a)
    y = r * math.sin(a)


    ponto_cartesiano = {}
    ponto_cartesiano['x'] = x
    ponto_cartesiano['y'] = y

    return ponto_cartesiano

raio = float(input())
angulo = float(input())

ponto_polar = {}
ponto_polar['r'] = raio
ponto_polar['a'] = angulo

print(ponto_polar)

ponto_cartesiano = converter(ponto_polar)

print(ponto_cartesiano)