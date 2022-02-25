saque = int(input('Quanto você quer sacar? R$'))
cedula1 = 1
cedula10 = 10
cedula20 = 20
cedula50 = 50
qt1 = qt10 = qt20 = qt50 = 0
conta = 0
while True:
    if saque > cedula50 and conta + cedula50 <= saque:
        qt50 += 1
        conta = cedula50 + conta
    elif saque > cedula20 and conta + cedula20 <= saque:
        qt20 += 1
        conta = cedula20 + conta
    elif saque > cedula10 and conta + cedula10 <= saque:
        qt10 += 1
        conta = cedula10 + conta
    elif saque > cedula1 and conta + cedula1 <= saque:
        qt1 += 1
        conta = cedula1 + conta
    if saque == conta:
        print('Sacando...')
        break

print(f'{qt50} notas de R$50')
print(f'{qt20} notas de R$20')
print(f'{qt10} notas de R$10')
print(f'{qt1} notas de R$1')
