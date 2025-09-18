tempo_segundos = int(input())


horas = tempo_segundos // 3600
tempo_segundos -= horas * 3600
minutos = tempo_segundos // 60
tempo_segundos -= minutos * 60
segundos = tempo_segundos


print(horas)
print(minutos)
print(segundos)

