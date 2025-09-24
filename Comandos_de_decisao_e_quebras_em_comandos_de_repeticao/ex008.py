num01 = float(input())
num02 = float(input())
operc = float(input())

if operc == 1 :
    print(f"{((num01+num02)/2):.2f}")
elif operc == 2 :
    if num01 > num02:
        print(f"{(num01-num02):.2f}")
    else:
        print(f"{(num02-num01):.2f}")
        
elif operc == 3 :
    print(f"{(num01*num02):.2f}")
elif operc == 4 :
    if num02 == 0:
        print("Erro")
    else:
        print(f"{(num01/num02):.2f}")
else:
    print("Erro")
