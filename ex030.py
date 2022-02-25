import math
numero = int(input('Digite um número inteiro qualquer: '))
resultado = numero % 2
if resultado == 0:
    print('{:.0f} é um número par'.format(numero))
else:
    print('{:.0f} é um número impar'. format(numero))