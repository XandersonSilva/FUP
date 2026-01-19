import math

def somar(z, w):
    resultado = {}
    resultado['real'] = z['real'] + w['real']
    resultado['imaginario'] = z['imaginario'] + w['imaginario']
    return resultado

def subtrair(z, w):
    resultado = {}
    resultado['real'] = z['real'] - w['real']
    resultado['imaginario'] = z['imaginario'] - w['imaginario']
    return resultado

def multiplicar(z, w):
    resultado = {}

    real_part = (z['real'] * w['real']) - (z['imaginario'] * w['imaginario'])
    imag_part = (z['real'] * w['imaginario']) + (z['imaginario'] * w['real'])
    
    resultado['real'] = real_part
    resultado['imaginario'] = imag_part
    return resultado

def modulo(c):

    return math.sqrt(c['real']**2 + c['imaginario']**2)

z_real = float(input())
z_imag = float(input())
z = {}
z['real'] = z_real
z['imaginario'] = z_imag

w_real = float(input())
w_imag = float(input())
w = {}
w['real'] = w_real
w['imaginario'] = w_imag

soma = somar(z, w)
subtracao = subtrair(z, w)
produto =   multiplicar(z, w)
modulo_z =  modulo(z)
modulo_w =  modulo(w)

print(soma)
print(subtracao)
print(produto)

print(f"{modulo_z:.2f}")
print(f"{modulo_w:.2f}")