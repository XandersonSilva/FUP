val =[]
for i in range(10):
    val.append((float(input())))

quad = []
for n in val:
    print(f"{n:.2f}")
for n in val:
    quad.append(n**2)
    print(f"{n**2:.2f}")
