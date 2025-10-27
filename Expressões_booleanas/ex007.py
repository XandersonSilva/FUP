def bissexto(ano):
    if(ano%400 == 0 or (ano%4 == 0 and ano%100 !=0)):
        print("Bissexto")
        return
    print("Nao bissexto")

ano = int(input())

bissexto(ano)
