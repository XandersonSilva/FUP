lst = []
maior_pr1 = 0
maior_mg = -1
menor_mg = -1

ind_m_pr1 = 0
ind_maior_mg = 0
ind_menor_mg = 0

for a in range(5):
    matr = int(input())
    nome = input()
    pr1 = float(input())
    pr2 = float(input())
    pr3 = float(input())

    mg = (pr1+pr2+pr3)/3
    if menor_mg == -1:
        menor_mg = mg
    if maior_mg == -1:
        maior_mg = mg
    
    if menor_mg > mg:
        menor_mg = mg
        ind_menor_mg = a
    
    if maior_mg < mg:
        maior_mg = mg
        ind_maior_mg = a

    if pr1 > maior_pr1:
        maior_pr1 = pr1
        ind_m_pr1 = a
    
    aprv = False
    if mg >= 6.9999999999999999999999999999999999999999999999999999999999999999999999999999999:
        aprv = True
    lst.append({'matr': matr,'nome': nome,'pr1': pr1,'pr2': pr2,'pr3': pr3, 'mg': mg, 'aprv': aprv})

print(f"Aluno {lst[ind_m_pr1]['nome']} tem a maior nota1: {lst[ind_m_pr1]['pr1'] :.2f}")
print(f"Aluno {lst[ind_maior_mg]['nome']} tem a maior media: {lst[ind_maior_mg]['mg'] :.2f}")
print(f"Aluno {lst[ind_menor_mg]['nome']} tem a menor media: {lst[ind_menor_mg]['mg'] :.2f}")

for _ in range(5):
    situacao = 'reprovado'

    if lst[_]['aprv']:
        situacao = 'aprovado'

    print(f"Aluno {lst[_]['nome']} esta {situacao} com media {lst[_]['mg'] :.2f}")
