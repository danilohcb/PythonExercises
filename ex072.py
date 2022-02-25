numerais = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito',
           'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
           'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    numero = int(input('Digite um número de 0 a 20: '))
    if 0 <= numero <= 20:
        print(f'Você digitou o número {numerais[numero]}')
        continua = str(input('Quer colocar outro número (S/N)? ')).upper().strip()[0]
        if continua == 'N':
            break
        while continua != 'S':
            continua = str(input('Quer colocar outro número (S/N)? ')).upper().strip()[0]
    if numero > 20 or numero < 0:
        print('Número inválido. Tente novamente!')
