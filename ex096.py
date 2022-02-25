def area(l, w):
    ar = l * w
    print(f'{ar}m²')


print('-' * 30)
print(f'{"Area Calculator!":^30}')
print('-' * 30)
length = float(input('Lenght (m): '))
width = float(input('Width (m): '))
area(length, width)
