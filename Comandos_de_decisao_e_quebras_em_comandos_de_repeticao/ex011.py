num01 = float(input())
operc = input()
num02 = float(input())

if operc == "+" :
    print(f"{(num01+num02):.2f}")
elif operc == "-" :
    print(f"{(num01-num02):.2f}")
elif operc == "*" :
    print(f"{(num01*num02):.2f}")
elif operc == "/" :
    if num02 == 0:
        print("Erro")
    else:
        print(f"{(num01/num02):.2f}")
else:
    print("Erro")
