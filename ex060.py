numero = int(input('Digite um número para ver o seu fatorial: '))
contagem = numero
print('{}! = '.format(numero), end='')
print('{} x'.format(numero), end=' ')

while contagem != 2:
    contagem -= 1
    print('{} x'.format(contagem), end=' ')
    numero = numero * contagem

print('1 =', end=' ')
print(numero)
