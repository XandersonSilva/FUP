num = int(input())

result = False
if num %5 == 0 or num % 3 == 0:
    if not (num %5 == 0 and num % 3 == 0):
        result = True
print(result)