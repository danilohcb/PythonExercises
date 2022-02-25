distancia = float(input('Digite a distância em KM que vai percorrer: '))
if distancia <= 200:
    valor = distancia * 0.50
    print('Você está prestes a começar uma viagem de {}Km'.format(distancia))
    print('E o valor a ser pago pela corrida é de R${:.2f}'.format(valor))
else:
    valor = distancia * 0.45
    print('Você está prestes a começar uma viagem de {}Km'.format(distancia))
    print('O valor a ser pago pela corrida é de R${:.2f}'.format(valor))
