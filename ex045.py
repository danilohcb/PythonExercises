import random
print('=' * 20, 'JOKENPÔ', '=' * 20)
jogador = input('Pedra, Papel ou Tesoura? ')
lista = ['pedra', 'papel', 'tesoura']
pc = random.choice(lista)

if jogador == 'pedra' or jogador == 'Pedra':
    print('Você usou\033[35m pedra\033[m.')
    print('O seu oponente usou\033[33m {}\033[m.'.format(pc))
    if pc == 'pedra':
        print('Vocês empataram!')
    if pc == 'papel':
        print('\033[31mVocê perdeu!\033[m')
    if pc == 'tesoura':
        print('\033[32mVocê venceu!\033[m')

if jogador == 'papel' or jogador == 'Papel':
    print('Você usou\033[35m papel\033[m.')
    print('O seu oponente usou\033[33m {}\033[m.'.format(pc))
    if pc == 'pedra':
        print('\033[32mVocê venceu!\033[m')
    if pc == 'papel':
        print('Vocês empataram!')
    if pc == 'tesoura':
        print('\033[31mVocê perdeu!\033[m')

if jogador == 'tesoura' or jogador == 'Tesoura':
    print('Você usou\033[35m tesoura\033[m.')
    print('O seu oponente usou\033[33m {}\033[m.'.format(pc))
    if pc == 'pedra':
        print('\033[31mVocê perdeu!\033[m')
    if pc == 'papel':
        print('\033[32mVocê venceu!\033[m')
    if pc == 'tesoura':
        print('Vocês empataram!')

print('=' * 20, 'JOKENPÔ', '=' * 20)
