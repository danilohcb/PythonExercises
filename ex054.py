from datetime import date
atual = date.today().year
maior = 0
menor = 0

for ano in range(1, 8):
    ano = int(input('Qual o ano de nascimento da {}ª pessoa? '.format(ano)))
    if atual - ano >= 21:
        maior += 1
    else:
        menor += 1

print('A quantidade de pessoas que já são maiores de idade é: {}'.format(maior))
print('A quantidade de pessoas que ainda são menores de idade é: {}'.format(menor))
