lista = list()
definitiva = list()

for n in range(0, 9):
    num = lista.append(int(input(f'Digite o {n + 1}º número: ')))
    definitiva.append(lista[:])
    lista.clear()

for num in definitiva[0:3]:
        print(f'{num}', end=' ',)
for num in definitiva[3:6]:
    if num == definitiva[3]:
        print(f'\n{num}', end=' ')
    else:
        print(f'{num}', end=' ')
for num in definitiva[6:9]:
    if num == definitiva[6]:
        print(f'\n{num}', end=' ')
    else:
        print(f'{num}', end=' ')
