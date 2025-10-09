def verificaAposenta(idade, servico):
    if idade >= 65:
        return "Pode se aposentar"
    if servico >= 30:
        return "Pode se aposentar"
    if idade >=60 and servico >=25:
        return "Pode se aposentar"
    return "Nao pode se aposentar"

idade = int(input())
servico = int(input())

print(verificaAposenta(idade, servico))