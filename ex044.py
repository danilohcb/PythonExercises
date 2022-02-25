preço = float(input('Informe o valor das compras: R$'))
print('Forma de pagamento:')
print('[ 1 ] À vista no dinheiro/cheque.')
print('[ 2 ] À vista no cartão.')
print('[ 3 ] Em até 2x no cartão.')
print('[ 4 ] 3x ou mais no cartão.')
opçao = int(input('Informe a forma de pagamento: '))

pg1 = preço - (preço * 0.1)
pg2 = preço - (preço * 0.05)
pg3 = preço
pg4 = preço + (preço * 0.2)

if opçao == 1:
    print('O valor da sua compra é de R${:.2f}'.format(pg1))
elif opçao == 2:
    print('O valor da sua compra é de R${:.2f}'.format(pg2))
elif opçao == 3:
    print('O valor da sua compra é de R${:.2f}'.format(pg3))
    print('Em 2x cada parcela será de R${:.2f}'.format(pg3 / 2))
elif opçao == 4:
    parcelas = int(input('Quantas parcelas serão?'))
    print('O valor da sua compra saíra por R${:.2f}'.format(pg4))
    print('Em {}x cada parcela será de R${:.2f}'.format(parcelas, pg4 / parcelas))
