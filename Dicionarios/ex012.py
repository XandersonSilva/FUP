lista_alunos = []

for i in range(10):
    nome = input()
    matricula = int(input())
    media = float(input())


    aluno = {}
    aluno['nome'] = nome
    aluno['matricula'] = matricula
    aluno['media'] = media

    lista_alunos.append(aluno)

aprovados = []
reprovados = []

for aluno in lista_alunos:
    if aluno['media'] >= 5.0:
        aprovados.append(aluno)
    else:
        reprovados.append(aluno)

for aluno in aprovados:
    print(aluno)

for aluno in reprovados:
    print(aluno)