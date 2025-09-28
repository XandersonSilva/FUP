txt = input()

inverso = ''
for i in range(len(txt) -1, -1, -1):
    if txt[i].lower() == 'a':
        inverso += '*'
        continue
    inverso += txt[i]
print(inverso)