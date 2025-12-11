def funcao(mat):
    result = 0
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] > 10:
                result += 1
    return result


mat = []
for i in range(4):
    mat.append([])
    for j in range(4):
        num = int(input(""))
        mat[i].append(num)
y = funcao(mat)
print(f"{y}")