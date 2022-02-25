lista = list()
boletim = list()
medias = list()
while True:
    nome = str(input('Digite o nome do ou da estudante: '))
    lista.append(nome)
    nota1 = float(input('Digite o valor da 1ª nota: '))
    nota2 = float(input('Digite o valor da 2ª nota: '))
    media = (nota1 + nota2) / 2
    medias.append(media)
    lista.append(nota1)
    lista.append(nota2)
    boletim.append(lista[:])
    lista.clear()
    continua = str(input('Deseja adicionar outra pessoa (S/N)? ')).upper().strip()[0]
    if continua in 'N':
        break
    while continua not in 'SN':
        continua = str(input('Comando inválido. Deseja adicionar outra pessoa (S/N)? ')).upper().strip()[0]

print('=' * 45)
print(f'{"Boletim":^45}')
print('=' * 45)
while True:
    pos = 0
    for n in range(0, len(boletim)):
        print(f'[{pos}] {boletim[n][0]:.<20} Media: [{medias[n]}]')
        pos += 1
    print('=' * 45)
    notas = int(input('Digite o número do aluno para ver as notas individuais(999 para sair): '))
    if notas <= pos:
        print(f'\033[035m{boletim[notas][0]:.<20} Notas: [{boletim[notas][1]}] [{boletim[notas][2]}]\033[m')
        print('~' * 50)
    if notas == 999:
        break
