cont = 0
num = int(input('Digite um valor para ver sua tabuada: '))

while True:
    cont += 1
    tabuada = num * cont
    print(f'{cont} x {num} = {tabuada}')
    if cont >= 10:
        cont = 0
        num = int(input('Digite um valor para ver sua tabuada: '))
        if num < 0:
            print('Programa finalizado.')
            break
