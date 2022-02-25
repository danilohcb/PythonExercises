c = int(input('Digite um número qualquer ou 999 para finalizar o programa: '))
n = 0
cont = 0
soma = 0

while c != 999:
    soma = n + c
    c = int(input('Digite outro número qualquer (999 = parar): '))
    n = soma
    cont += 1

print('Você digitou {} números e a soma entre eles foi {}'.format(cont, soma))
