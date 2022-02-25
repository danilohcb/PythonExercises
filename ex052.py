num = int(input('Informe um número inteiro: '))
contador = 0

for c in range(1, num + 1):
    if num % c == 0:
        print('\033[033m', end='')
        contador += 1
    else:
        print('\033[031m', end='')
    print(c, end=' ')
print('\n\033[mO número {} pode ser dividido {} vezes'.format(num, contador))
if contador == 2:
    print('E por isso ele é um número primo!')
else:
    print('E por isso ele não é um número primo!')
