from time import sleep
lista = list()
cont = 0
while True:
    num = lista.append(int(input('Digite um valor: ')))
    cont += 1
    continua = str(input('Deseja continuar (S/N)? ')).strip().upper()[0]
    while continua not in 'SN':
        print('Comando inválido, tente novamente.')
        continua = str(input('Deseja continuar (S/N)? ')).strip().upper()[0]
    if continua == 'N':
        print('Encerrando...')
        sleep(1)
        break

print('=-' * 30)
print(f'A lista criada foi: {lista}')
print('=-' * 30)
print(f'O número 5 apareceu na posição: ', end='')
for pos, n in enumerate(lista):
    if n == 5:
        print(f'{pos + 1}', end=' ')
    if 5 not in lista:
        print('\033[031mO número 5 não está na lista.\033[m', end='')
        break

lista.sort(reverse=True)
print(f'\nForam digitados {cont} números na lista.'
      f'\nEsta é a lista em ordem decrescente: {lista}')

