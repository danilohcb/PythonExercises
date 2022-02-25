lista = list()
ficha = list()
maior = menor = 0

while True:
    nome = lista.append(str(input('Digite seu nome: ')))
    peso = lista.append(float(input('Digite seu peso: ')))
    if len(ficha) == 0:
        maior = menor = lista[1]
    else:
        if lista[1] > maior:
            maior = lista[1]
        if lista[1] < menor:
            menor = lista[1]
    ficha.append(lista[:])
    lista.clear()
    continua = str(input('Deseja adicionar outra pessoa (S/N)? ')).upper().strip()[0]
    while continua not in 'SN':
        continua = str(input('Comando inválido. Deseja continuar (S/N)? ')).upper().strip()[0]
    if continua == 'N':
        break

print(ficha)
print(f'O número de pessoas cadastradas foi de {len(ficha)} pessoas.')
print(f'O maior peso cadastrado foi {maior}. Peso de ', end='')
for n in ficha:
    if n[1] == maior:
        print(f'[{n[0]}] ', end='')
print(f'\nO menor peso cadastrado foi {menor}. Peso de ', end='')
for n in ficha:
    if n[1] == menor:
        print(f'[{n[0]}] ', end='')
