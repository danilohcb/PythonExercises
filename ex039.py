from datetime import date
nascimento = int(input('Informe o ano do seu nascimento: '))
sexo = input('Informe seu sexo: ')
atual = date.today().year
idade = atual - nascimento

if sexo == 'm' or sexo == 'M':
    print('Masculino')
    if idade < 18:
        print('Quem nasceu em {} tem {} anos'.format(nascimento, idade))
        print('Faltam {} anos para o seu alistamento.'.format(18 - idade))
        print('Você ainda não precisa se alistar! seu alistamento será em {}'.format(nascimento + 18))
    elif idade > 18:
        print('Quem nasceu em {} tem {} anos'.format(nascimento, idade))
        print('Já se passaram {} anos do seu alistamento'.format(idade - 18))
        print('Seu alistamento foi em {}'.format(nascimento + 18))
    else:
        print('Quem nasceu em {} tem {} anos'.format(nascimento, idade))
        print('Você deve se alistar imediatamente!')

elif sexo == 'f' or sexo == 'F':
    print('Feminino')

