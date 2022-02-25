contIdade = 0
contH = 0
contM = 0
while True:
    print('-' * 30)
    print('-REGISTRO-'.center(25))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (M/F): ')).upper().strip()[0]
    while sexo not in 'MF':
        sexo = str(input('Sexo (M/F): ')).upper().strip()[0]
    print('-' * 30)
    adicionar = str(input('Deseja adicionar mais um registro, Sim ou Não?(S/N) ')).upper().strip()[0]
    if idade >= 18:
        contIdade += 1
    if sexo == 'M':
        contH += 1
    if idade < 20 and sexo == 'F':
        contM += 1
    while adicionar not in 'SN':
        adicionar = str(input('Deseja adicionar mais um registro, Sim ou Não?(S/N) ')).upper().strip()[0]
    if adicionar == 'N':
        print('Encerrando...')
        break

print('-' * 30)
print('Programa encerrado.')
print(f'{contIdade} pessoas são maiores de 18 anos.')
print(f'{contH} homens foram cadastrados.')
print(f'{contM} mulheres são menores de 20 anos.')
