lista = [int(input('Digite um valor: ')), int(input('Digite outro valor: ')),
         int(input('Digite outro valor: ')), int(input('Digite outro valor: ')),
         int(input('Digite o último valor: '))]
print(lista)
print(f'O maior número da lista foi {max(lista)} na posiçao ', end='')
for c, n in enumerate(lista):
    if n == max(lista):
        print(f'{c + 1}', end=' ')

print(f'\nO menor número da lista foi {min(lista)} na posição ', end='')
for c, n in enumerate(lista):
    if n == min(lista):
        print(f'{c + 1}', end=' ')

# Cometario do video, ótimo jeito de fazer.
'''a = [input(f'Digite um valor para a posição {i}: ') for i in range(0, 5)]
posmax = []
posmin = []
for pos, valor in enumerate(a):
    if valor == max(a):
        posmax.append(pos)
    elif valor == min(a):
        posmin.append(pos)
print(f'O maior valor foi {max(a)}, e está na posição {posmax}')
print(f'O menor valor foi {min(a)}, e está na posição {posmin}')'''
