n1 = int(input('Digite o primeiro número inteiro: '))
n2 = int(input('Digite o segundo número inteiro: '))

if n1 > n2:
    print('O número {} é maior que {}!'.format(n1, n2))
elif n1 < n2:
    print('O número {} é maior que {}!'.format(n2, n1))
else:
    print('O dois números são iguais!')