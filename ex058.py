import random
import time
print('=' * 40)
print('JOGO DO ADIVINHA')
print('Tente adivinhar um número de 0 a 10!')
print('=' * 40)

tentativas = 1
aleatorio = random.randint(0, 10)
palpite = int(input('Qual número o computador pensou? '))

while palpite != aleatorio:
    print('\033[033mPROCESSANDO...\033[m')
    time.sleep(2)
    palpite = int(input('Você errou, tente novamente: '))
    tentativas += 1
    if palpite == aleatorio:
        print('\033[033mPROCESSANDO...\033[m')
        time.sleep(2)
        print('Parabéns você acertou! Você precisou de {} tentativas!'.format(tentativas))
        tentativas += 1
