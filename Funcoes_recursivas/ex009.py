def fat(f):
    if f == 0:
        return 1
    else:
        return f * fat(f-1)

def sf(x):
    if x == 0:
        return 1
    else:
        return fat(x) * sf(x-1)


x = int(input(""))
y = sf(x)
print(f"{y}")