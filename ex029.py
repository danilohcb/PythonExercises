velocidade = int(input('Qual a velocidade que o carro está? '))
multa = (velocidade - 80) * 7

if velocidade <= 80:
    print('Tenha um bom dia e dirija com segurança!')
else:
    print('Você está excedendo a velocidade da via de 80km/h!!')
    print('Uma multa será cobrada no valor de R${:.2f}!'.format(multa))
