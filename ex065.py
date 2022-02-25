num = int(input('Digite um número inteiro ou digite 0 para finalizar: '))
x = 0
cont = 0
soma = 0

menor = num
maior = num

while num != 0:
    soma = num + x
    x = soma
    num = int(input('Digite um número inteiro ou digite 0 para finalizar: '))
    cont += 1
    if menor > num and num != 0:
        menor = num
    if maior < num:
        maior = num


while num == 0:
    continua = str(input('Deseja continuar digitando? [S] ou [N] ')).lower()
    if continua == 'n':
        print('\033[033mFinalizando...\033[m')
        break
    elif continua == 's':
        num = int(input('Digite um número inteiro ou digite 0 para finalizar: '))
        while num != 0:
            soma = num + x
            x = soma
            num = int(input('Digite um número inteiro ou digite 0 para finalizar: '))
            cont += 1
            if menor > num and num != 0:
                menor = num
            if maior < num:
                maior = num

media = soma / cont
print('O total dos número digitados foi {} e a média é {}'.format(soma, media))
print('O menor número digitado foi {} e o maior foi {}'.format(menor, maior))
