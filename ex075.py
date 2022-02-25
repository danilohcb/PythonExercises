numeros = (int(input('Digite um valor de 0 a 10: ')), int(input('Digite um valor de 0 a 10: ')),
           int(input('Digite um valor de 0 a 10: ')), int(input('Digite um valor de 0 a 10: ')))

print(f'O valor 9 apareceu {numeros.count(9)}x.')
if 3 in numeros:
    print(f'O primeiro valor 3 foi digitado na {numeros.index(3) + 1}ª posição.')
else:
    print('Não houve nenhum número 3.')
print('Os valores pares digitados foram: ', end='')
'''if numeros[0] % 2 == 0:
    print(f'{numeros[0]}', end=' ')
if numeros[1] % 2 == 0:
    print(f'{numeros[1]}', end=' ')
if numeros[2] % 2 == 0:
    print(f'{numeros[2]}', end=' ')
if numeros[3] % 2 == 0:
    print(f'{numeros[3]}', end=' ')'''
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')
