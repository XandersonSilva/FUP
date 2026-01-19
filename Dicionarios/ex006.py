lst = []

for _ in  range(2):
    x = float(input())
    y = float(input())
    z = float(input())
    
    lst.append({'x': x, 'y': y, 'z': z})

result = {  'x': (lst[0]['x'] + lst[1]['x']) ,
            'y': (lst[0]['y'] + lst[1]['y']) ,
            'z': (lst[0]['z'] + lst[1]['z']) }

print(result)