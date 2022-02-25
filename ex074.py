from random import randint
numeros = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))

print('Os números sorteados foram: ', end='')
for c in numeros:
    print(c, end='  ')

print(f'\nE o maior número foi o {max(numeros)}'
      f'\nE o menor número foi o {min(numeros)}')






'''n1 = randint(0, 20)
n2 = randint(0, 20)
n3 = randint(0, 20)
n4 = randint(0, 20)
n5 = randint(0, 20)

numeros = (n1, n2, n3, n4, n5)

maior = menor = n1
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3
if n4 > maior:
    maior = n4
if n5 > maior:
    maior = n5

if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3
if n4 < menor:
    menor = n4
if n5 < menor:
    menor = n5
print(numeros)
print(maior)
print(menor)'''
