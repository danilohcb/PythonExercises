'''sexo = str(input('Informe seu sexo (M/F): '))

while sexo != 'M' or sexo != 'F':
    sexo = str(input('Sexo invalido. Por favor digite M ou F: ')).upper()
    if sexo == 'M':
        print('Sexo masculino validado!')
        break
    elif sexo == 'F':
        print('Sexo feminino validado!')
        break'''

sexo = str(input('Informe seu sexo (M/F): ')).upper().strip()[0]

while sexo not in 'MF':
    sexo = str(input('Sexo inválido. Por favor digite M ou F: ')).upper().strip()[0]
print('Sexo {} validado!'.format(sexo))
