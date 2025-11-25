def e_primo(n):
    if n < 0:
        n = -n
    if n == 0 or n == 1:
        return False
    if (n == 2 or
        n == 3 or 
        n == 5 or
        n == 7):
        return True
    if n % 2 == 0:
        return False
    
    limite = int(n ** (1/2))
    if n % limite == 0:
        return False
    
    for d in range(3, limite + 1, 2):
        if d % 3 == 0 or d % 5 == 0 or d % 7 == 0:
            continue
        if n % d == 0:
            return False
    return True


entrada = []

for _ in range(10):
    entrada.append(int(input()))
result = []
for i in range(len(entrada)):
    if e_primo(entrada[i]):
        result.append(entrada[i])
        result.append(i)
for i in range(0, len(result)-1, 2):
    print(result[i])
    print(result[i+1])
