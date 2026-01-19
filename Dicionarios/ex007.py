
qtd_str = input()
qtd_alunos = int(qtd_str)

lista_alunos = []
for i in range(qtd_alunos):
    matricula = int(input())
    nome = input()
    codigo = input()
    nota1 = float(input())
    nota2 = float(input())

    media = (nota1 * 1.0 + nota2 * 2.0) / 3.0

    aluno = {}
    aluno['matricula'] = matricula
    aluno['nome'] = nome
    aluno['codigo'] = codigo
    aluno['nota1'] = nota1
    aluno['nota2'] = nota2
    aluno['media'] = media

    lista_alunos.append(aluno)
for aluno in lista_alunos:
    print(aluno)