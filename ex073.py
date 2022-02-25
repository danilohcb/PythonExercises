times = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragantino',
         'Fluminense', 'América-MG', 'Atlético-GO', 'Santos', 'Ceará', 'Internacional',
         'São Paulo', 'Athletico-PR', 'Cuiabá', 'Juventude', 'Grêmio', 'Bahia', 'Sport', 'Chapecoense')

print(f'Os 5 primeiros times da tabela são: \n {times[:5]}')
print('=-' * 50)
print(f'Os últimos 4 colocados da tabela são: \n {times[-4:]}')
print('=-' * 50)
print(f'Os times da tabela em ordem alfabética são: \n {sorted(times)}')
print('=-' * 50)
print(f'O time da Chapecoense está na {times.index("Chapecoense") + 1}ª posição.')
