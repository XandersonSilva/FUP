text = input()
letra = input()
result = ''
contador = 0

for l in text:
    l_min = l.lower()
    if l_min == "a" or l_min == "e" or l_min == "i" or l_min == "o" or l_min == "u":
        result += letra
        contador += 1
        continue
    result += l
print(contador)
print(result)
