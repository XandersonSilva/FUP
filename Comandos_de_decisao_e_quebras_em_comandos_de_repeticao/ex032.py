x01 = int(input())
x02 = int(input())

menor = x01
maior = x02

if x01 > x02:
    menor = x02
    maior = x01

quociente = 0

for i in range(1, maior +1):
    if i * menor > maior:
        break
    if i * menor == maior:
        quociente = i
    quociente = i
print(quociente)