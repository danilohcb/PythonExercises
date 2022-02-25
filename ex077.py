palavras = ('arara', 'azul', 'caderno', 'celular', 'prato', 'natureza', 'viagem', 'curso')
for c in palavras:
    print(f'\nNa palavra {c}, as vogais são: ', end='')
    for letras in c:
        if letras in 'aeiou':
            print(letras, end=' ')
