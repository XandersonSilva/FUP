nome = input()
idade = int(input())
sexo = input()
cpf = input()
data_nascimento = input()
codigo_setor = int(input())
cargo = input()
salario = float(input())

funcionario = {}
funcionario['nome'] = nome
funcionario['idade'] = idade
funcionario['sexo'] = sexo
funcionario['cpf'] = cpf
funcionario['nascimento'] = data_nascimento
funcionario['setor'] = codigo_setor
funcionario['cargo'] = cargo
funcionario['salario'] = salario

print(funcionario)