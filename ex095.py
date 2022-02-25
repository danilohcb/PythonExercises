time = list()
dados = dict()
resultados = list()
total = 0
while True:
    dados.clear()
    dados['jogador'] = str(input('Nome do jogador: '))
    partidas = int(input('Numero de partidas: '))
    resultados.clear()
    for g in range(0, partidas):
        resultados.append(int(input(f'   Quantos gols na partida {g + 1}? ')))
    dados['gols'] = resultados[:]
    dados['total'] = sum(resultados)
    time.append(dados.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
        if resp in 'SN':
            break
        print('Erro. Responda apenas S ou N.')
    if resp == 'N':
        break
print('=-' * 30)
print('cod', end='  ')
for i in dados.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
