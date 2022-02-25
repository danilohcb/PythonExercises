lista = list()
pares = list()
impares = list()

while True:
    num = lista.append(int(input('Digite um valor: ')))
    continua = str(input('Deseja continuar (S/N)? ')).upper().strip()[0]
    while continua not in 'SN':
        print('Comando inválido, tente novamente.')
        continua = str(input('Deseja continuar (S/N)? ')).upper().strip()[0]
    if continua == 'N':
        break
for num in lista:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print(f'A lista criada e completa é: {lista}')
pares.sort()
print(f'A lista apenas com os números pares é: {pares}')
impares.sort()
print(f'A lista apenas com os números ímpares é: {impares}')
