numerador = 1
resultado = 0
for i in range(1, 51):
    resultado += numerador/i
    numerador += 2
print(f"{resultado:.10f}")