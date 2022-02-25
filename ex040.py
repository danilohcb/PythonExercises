n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
med = (n1 + n2) / 2

if med < 5:
    print('Sua média foi de {:.1f}'.format(med))
    print('Você foi reprovado!')
elif med >= 5 and med < 7:
    print('Sua média foi de {:.1f}'.format(med))
    print('Você está de recuperação!')
elif med >= 7:
    print('Sua média foi de {:.1f}'.format(med))
    print('Parabéns! Você foi aprovado!')

