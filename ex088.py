from random import randint
from time import sleep
'''lista = []
sorteio = list()
jogos = (int(input('Quantos jogos você quer fazer? ')))
cont = 0
while True:
    for n in range(0, 6):
        lista.append(randint(1, 60))
        sorteio.append(lista[:])
        lista.pop()
        sorteio.sort()
    print(f'Jogo {cont + 1}...')
    for num in sorteio:
        print(num, end=' ')
    print()
    sorteio.clear()
    cont += 1
    sleep(1)
    if cont == jogos:
        break'''

# Better way (Sem repetir numeros)
lista = []
sorteio = []
print('\033[033m=\033[m' * 35)
print(f'\033[033m{"Lottery!":^35}\033[m')
print('\033[033m=\033[m' * 35)
jogos = (int(input('Quantos jogos você quer fazer? ')))
print('~' * 35)
total = 1
while total <= jogos:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    sorteio.append(lista[:])
    lista.clear()
    for num in sorteio:
        print(f'Jogo {total}: {num}')
    sleep(1)
    sorteio.clear()
    total += 1
