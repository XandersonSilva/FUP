x = input()
novo_txt = ''
for i in range(len(x)):
    if x[i] == '0':
        novo_txt += "1"
    else:
        novo_txt += x[i]
print(novo_txt)
