valor1 = int(input('Digite um valor: '))
valor2 = int(input('Digite outro valor: '))
opçao = 0
while opçao != 5:
    print('-' * 40)
    print('[ 1 ] Somar'
          '\n[ 2 ] Multiplicar'
          '\n[ 3 ] Maior'
          '\n[ 4 ] Novos Números'
          '\n[ 5 ] Sair do programa')
    print('-' * 40)
    opçao = int(input('Digite o número da opção desejada: '))
    if opçao == 1:
        soma = valor1 + valor2
        print('A soma entre {} e {} é {}'.format(valor1, valor2, soma))
    elif opçao == 2:
        mult = valor1 * valor2
        print('A multiplicação entre {} e {} é {}'.format(valor1, valor2, mult))
    elif opçao == 3:
        if valor1 > valor2:
            maior = valor1
        else:
            maior = valor2
        print('Entre {} e {} o maior valor é {}'.format(valor1, valor2, maior))
    elif opçao == 4:
        valor1 = int(input('Digite um valor: '))
        valor2 = int(input('Digite outro valor: '))
    elif opçao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida.')
print('FIM')

'''soma = valor1 + valor2
mult = valor1 * valor2
if valor1 > valor2:
    maior = valor1
    menor = valor2
else:
    maior = valor2
    menor = valor1

while user == 4:
    valor1 = float(input('Digite um valor: '))
    valor2 = float(input('Digite outro valor: '))
    print('-' * 40)
    print('[ 1 ] Somar'
          '\n[ 2 ] Multiplicar'
          '\n[ 3 ] Maior'
          '\n[ 4 ] Novos Números'
          '\n[ 5 ] Sair do programa')
    print('-' * 40)
    user = int(input('Digite o número da opção desejada: '))
    if user == 1:
        print(soma)
    elif user == 2:
        print(mult)
    elif user == 3:
        print('{} é maior que {}'.format(maior, menor))
    elif user == 5:
        print('FIM')
    elif user > 5 or user <= 0:
        print('Opção inválida')'''
