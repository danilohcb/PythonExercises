largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura * altura
print('Sua parede tem dimensão de {}x{} e sua área é de {:.3f}m².'.format(largura, altura, area))
print('Para pintar essa parede, você vai precisar de {}l de tinta.'.format(area / 2))
