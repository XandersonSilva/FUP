texto = input()
letra_procurada = input()
inicio_da_procura = int(input())

parte_nao_procurada = texto[:inicio_da_procura]
parte_nao_procurada = parte_nao_procurada.replace(letra_procurada, "¬")
novo_texto = texto[inicio_da_procura:]

novo_texto = parte_nao_procurada + novo_texto

print(novo_texto.find(letra_procurada))
