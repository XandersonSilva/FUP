def funcao(a, b, c):
    if a >(b+c) or b > (a+ c) or c > (a+b):
        print("Nao triangulo")
        return
    if a == b and b == c:
        print("Triangulo equilatero")
        return
    if a == b or c == a or c == b:
        print("Triangulo isosceles")
        return
    print("Triangulo escaleno")


a = int(input())
b = int(input())
c = int(input())

funcao(a, b, c)