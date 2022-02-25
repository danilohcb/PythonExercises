numero = int(input('Digite um número para ver sua tabuada: '))
for tabuada in range(1, 11):
    resultado = tabuada * numero
    print(tabuada, 'x', numero, '=', resultado)
