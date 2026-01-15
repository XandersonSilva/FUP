alunos = []
n_alunos = int(input())

for a in range(n_alunos):
    nome = input()
    matricula = int(input())
    curso = input()
    alunos.append({'nome': nome, 'matricula': matricula, 'curso': curso})

for a in range(n_alunos):
    print(alunos[a])
