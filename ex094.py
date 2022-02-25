galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper().strip()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Erro! Digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma = soma + pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if resp in 'SN':
            break
        print('Erro! Digite apenas S ou N.')
    if resp == 'N':
        break
print('=-' * 30)
print(f'Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'A média das idades é de {media:5.2f}')
print('As mulheres cadastradas foram: ', end=' ')
for p in galera:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ', end='')
print()
print('Lista das pessoas que estão acima da média das idades: ', end=' ')
for p in galera:
    if p['idade'] >= media:
        print(f'{p["nome"]} ', end='')
print()

