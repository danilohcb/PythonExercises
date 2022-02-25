cont = 0
soma = 0
while True:
    num = int(input('Digite um número inteiro (999 para parar): '))
    if num == 999:
        print(f'Você digitou {cont} número e a soma entre eles é {soma}')
        break
    soma += num
    cont += 1
