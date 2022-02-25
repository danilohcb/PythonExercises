lista = list()
definitiva = list()
pares = list()
par = resultado = 0

for n in range(0, 9):
    num = (int(input(f'Digite o {n + 1}º número: ')))
    lista.append(num)
    definitiva.append(lista[:])
    if num % 2 == 0:
        resultado = par + num
        par = resultado
    lista.clear()

for num in definitiva[0:3]:
    print(f'{num}', end=' ', )
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

print()
print('-=' * 40)
print(f'O resultado de todos os números pares da matriz é: {resultado}')
coluna3 = definitiva[2] + definitiva[5] + definitiva[8]
coluna = 0
for n in coluna3:
    resultado = coluna + n
    coluna = resultado
print(f'O resultado dos números da terceira coluna é {resultado}')
linha2 = definitiva[3] + definitiva[4] + definitiva[5]
print(f'O maior valor da segunda linha é {max(linha2)}')
