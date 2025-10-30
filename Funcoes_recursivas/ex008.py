def SomaSerie(x1, x2, x3):
    if x1 > x2:
        return 0
    elif x1 + x3 > x2:
        return x1
    else:
        return x1 + SomaSerie(x1 + x3, x2, x3)



x1 = int(input(""))
x2 = int(input(""))
x3 = int(input(""))
y = SomaSerie(x1, x2, x3)
print(f"{y}")