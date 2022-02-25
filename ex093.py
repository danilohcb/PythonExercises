dados = dict()
resultados = list()
total = 0
dados['jogador'] = str(input('Nome do jogador: '))
partidas = int(input('Numero de partidas: '))
for g in range(0, partidas):
    gols = int(input(f'   Quantos gols na partida {g + 1}? '))
    resultados.append(gols)
    total = total + gols
dados['gols'] = resultados[:]
dados['total'] = total
print('=-' * 30)
print(dados)
print('=-' * 30)
for k, v in dados.items():
    print(f'{k} tem o valor de {v}')
print('=-' * 30)
print(f'O jogador {dados["jogador"]} jogou {partidas} partidas.')
for n in range(0, len(resultados)):
    print(f' => Na partida {n + 1}, fez {resultados[n]} gols')
