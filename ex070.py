maiormil = 0
nome = str(input('Nome do produto: '))
preço = float(input('Valor do produto: R$'))
total = preço
menorP = preço
menorN = nome

while True:
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Deseja continuar inserindo produtos? (S/N)')).upper().strip()[0]
    if continua == 'N':
        print('Fechando a conta...')
        print(f'O total da compra foi de \033[033mR${total}\033[m.')
        print(f'Número de produtos acima de R$1000,00: \033[033m{maiormil}\033[m.')
        print(f'O nome do produto de menor preço é \033[033m{menorN}\033[m.')
        break
    else:
        nome = str(input('Nome do produto: '))
        preço = float(input('Valor do produto: R$'))
        total += preço
        if menorP > preço:
            menorP = preço
            menorN = nome
        if preço >= 1000:
            maiormil += 1

'''while True:
    nome = str(input('Nome do produto: '))
    preço = float(input('Valor do produto: R$'))
    total += preço
    if menorP > preço:
        menorP = preço
        menorN = nome
    if preço >= 1000:
        maiormil += 1
    continua = str(input('Deseja continuar inserindo produtos? (S/N)')).upper().strip()[0]
    while continua not in 'SN':
        continua = str(input('Deseja continuar inserindo produtos? (S/N)')).upper().strip()[0]
    if continua == 'N':
        print('Fechando a conta...')
        break


print(f'O total da compra foi de R${total}.')
print(f'Número de produtos acima de R$1000,00: {maiormil}.')
print(f'O nome do produto de menor preço é {menorN}.')'''
