def fazer_conta(x, y, z):
    if x == 1 :
        print(f"{(y+z):.2f}")
    elif x == 2 :
        print(f"{(y-z):.2f}")
    elif x == 3 :
        print(f"{(y*z):.2f}")
    elif x == 4 :
        print(f"{(y/z):.2f}")
    


continuar = 1
while(continuar == 1):
    print('''1 - Adicao
2 - Subtracao
3 - Multiplicacao
4 - Divisao
5 - Saida''')
    
    operacao = float(input())
    if operacao == 5:
        continuar = 0
        continue
    fazer_conta(operacao, float(input()), float(input()))
