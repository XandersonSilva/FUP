def funcao(x, y):
    result = ''
    for i in range(len(x)):
        if x[i] == ' ':
            result += ' '
            continue
        if ord(x[i]) + y > 90:
            result += chr(((ord(x[i]) + y) - 26))
            continue
        if ord(x[i]) + y > 122:
            result += chr(((ord(x[i]) + y) - 26))
            continue
        result += chr(ord(x[i]) + y)
    return result
