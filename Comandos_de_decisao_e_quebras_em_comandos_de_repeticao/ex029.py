num = int(input())
divisores = 0


for i in range(1, num+1):
    if num%i == 0:
        divisores += 1
    if divisores > 2:
        print("Nao primo")
        break

if num == 1:
    print("Nao primo")
elif divisores <= 2:
    print("Primo")
