def file(name='', score=''):
    print('   Name', end='')
    print(f'{"Score":>30}')
    print('-=' * 20)
    print(f'   {name} {score:>25}')


player = str(input('Player"s name: ')).strip()
if player == '':
    player = '<Unknown>'
points = str(input('Score: ')).strip()
if points == '':
    points = 0
file(player, points)
