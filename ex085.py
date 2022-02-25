numeros = list()
pares = list()
impares = list()

for n in range(0, 7):
    valores = numeros.append(int(input(f'Digite o {n + 1}º valor: ')))

for valores in numeros:
    if valores % 2 == 0:
        pares.append(valores)
    else:
        impares.append(valores)

numeros.clear()
pares.sort()
impares.sort()
numeros.append(pares)
numeros.append(impares)

print('~' * 50)
for divisao in numeros:
    print(f'A lista de números pares é: {numeros[0]}')
    print(f'A lista de números ímpares é: {numeros[1]}')
    break

