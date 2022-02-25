produto = ('Mouse', 80, 'Teclado', 200, 'Monitor', 1200, 'Webcam', 350, 'Headset', 250)
print('=' * 45)
print(f'{"Lojas Danilo":^40}')
print('=' * 45)
'''print(f'{produto[0]}............................R${produto[1]:.2f}'
      f'\n{produto[2]}..........................R${produto[3]:.2f}'
      f'\n{produto[4]}..........................R${produto[5]:.2f}'
      f'\n{produto[6]}...........................R${produto[7]:.2f}'
      f'\n{produto[8]}..........................R${produto[9]:.2f}')'''
for c in range(0, len(produto)):
    if c % 2 == 0:
        print(f'{produto[c]:.<30}', end='')
    else:
        print(f'R${produto[c]:>.2f}')
print('=' * 45)
