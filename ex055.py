maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('Informe o peso da {}ª pessoa: '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    elif peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso

print('O maior peso é de {}Kg'.format(maior))
print('O menor peso é de {}Kg'.format(menor))
