p = float(input('Digite o preço do produto: R$'))
desc = p * 0.05
valorDesc = p - desc
print('O valor deste produto com 5% de desconto é de: R${:.2f}'.format(valorDesc))
