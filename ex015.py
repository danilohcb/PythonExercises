dias = int(input('Quantos dias você ficou com o carro? '))
km = float(input('Quantos km você percorreu? '))
total = (km * 0.15) + (dias *60)
print('o preço a pagar pelo aluguel do carro é o valor de R${:.2f}'.format(total))
