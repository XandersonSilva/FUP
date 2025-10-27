def funcao(x):    
    if x[2] == "/" and x[5] == "/":
        if (x[:2].isnumeric() and (x[:2].find("/") == -1)) and (x[3:5].isnumeric() and (x[3:5].find("/") == -1)) and (x[6:].isnumeric() and (x[6:].find("/") == -1) and len(x[6:]) == 4):
            return int(x[:2]), int(x[3:5]), int(x[6:])

    return 0, 0, 0
