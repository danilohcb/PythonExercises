frase = input('Digite uma palavra ou frase para saber se é um palindromo: ').strip().upper()
palavras = frase.split()
letras = ''.join(palavras)
inverso = ''

for c in range(len(letras) - 1, -1, -1):
    inverso += letras[c]

print('A palavra ou frase escrita foi "{}"'.format(letras))

if letras == inverso:
    print('de trás pra frente fica "{}", é um palindromo!'.format(inverso))
else:
    print('de trás pra frente fica "{}", não é um palindromo!'.format(inverso))

