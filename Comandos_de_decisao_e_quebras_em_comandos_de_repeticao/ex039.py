def ordem_alfa(x, y):
    x_c = x.replace(" ", "") 
    y_c = y.replace(" ", "") 
    if len(x_c) != len(y_c):
        if len(x_c) > len(y_c):
            return y_c
        return x_c
    
    for i in range(len(x_c)):
        if x_c[i] != y_c[i]:
            if ord(x_c[i]) < ord(y_c[i]):
                return x
            return y
    return x
a = input()
b = input()

print(ordem_alfa(a, b))