def retira_nao_letra(x):
    novo_txt = ''
    for l in range(len(x)):
        if ord(x[l]) > 64:
            if ord(x[l]) <91:
                novo_txt += x[l]
        if ord(x[l]) > 96:
            if ord(x[l]) <123:
                novo_txt += x[l]
    return novo_txt


txt = input()

txt = retira_nao_letra(txt.lower())
inverso = ''
for i in range(len(txt) -1, -1, -1):
    inverso += txt[i]

if txt == inverso:
    print(True)
else:
    print(False)