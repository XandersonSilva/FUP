def simplificar(x1, x2):
    maior = x1+1
    if x2>x1:
        maior = x2+1

    for i in range(maior, 1, -1):
        if x1%i ==0:
            if x2%i==0:
                return (x1//i), (x2//i)
    return x1, x2
