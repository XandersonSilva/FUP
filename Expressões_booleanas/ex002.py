text = input()
result = ''

for l in text:
    l_min = l.lower()
    if l_min == "a" or l_min == "e" or l_min == "i" or l_min == "o" or l_min == "u":
        continue
    result += l
print(result)
