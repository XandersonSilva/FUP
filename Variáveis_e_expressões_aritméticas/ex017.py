val_01 = float(input())
val_02 = float(input())
val_03 = float(input())
premio = float(input())

valor_investido = val_01 + val_02 + val_03

partes_iguais = premio / valor_investido

ganhador_01 = partes_iguais * val_01
ganhador_02 = partes_iguais * val_02
ganhador_03 = partes_iguais * val_03



print(f"{ganhador_01:.2f}")
print(f"{ganhador_02:.2f}")
print(f"{ganhador_03:.2f}")
