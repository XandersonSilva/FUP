n = input()
resultado = ""
for i in range(len(n)):
    resultado += chr(ord(n[i])+1)
print(resultado)
