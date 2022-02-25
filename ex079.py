lista = []
lista.append(int(input('Digite um número: ')))
while True:
    continua = str(input('Deseja continuar (S/N)? ')).upper().strip()[0]
    while continua not in 'SN':
        continua = str(input('Comando inválido. Deseja continuar (S/N)? ')).upper().strip()[0]
    if continua == 'S':
        lista.append(int(input('Digite outro número: ')))
        for n in lista:
            if lista.count(n) > 1:
                lista.pop()
                print('Número repetido não será adicionado, adicione outro número.')
    elif continua == 'N':
        print('Encerrando...')
        print(f'Os número digitados em ordem crescente são {sorted(lista)}')
        break

