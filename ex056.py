idades = 0
maior = ''
velho = 0
contador = 0
for c in range(1, 5):
    print('-' * 40)
    nome = str(input('Informe seu nome: '))
    idade = int(input('Informe sua idade: '))
    sexo = str(input('Informe seu sexo (H ou M): '))
    idades = idades + idade
    if idade < 20 and sexo == 'M' or sexo == 'm' and idade < 20:
        contador += 1

    if sexo == 'H' and velho < idade or sexo == 'h' and velho < idade:
        maior = nome
        velho = idade

media = idades / 4
print('O nome do homem mais velho é {} e sua idade é {}'.format(maior, velho))
print('A média das idades do grupo é {}'.format(media))
print('O número de mulheres abaixo de 20 anos é de {}'.format(contador))
