premio = float(input())

primeiro_lugar = premio * 0.46
segundo_lugar = premio * 0.32
terceiro_lugar = premio - primeiro_lugar - segundo_lugar


print(f"{primeiro_lugar:.2f}")
print(f"{segundo_lugar:.2f}")
print(f"{terceiro_lugar:.2f}")
