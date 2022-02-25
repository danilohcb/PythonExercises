import random
import time
print('-=-' * 20)
print('Vou pensar em um número entre 0 a 5. Tente adivinhar...')
print('-=-' * 20)
numeroPensado = random.randint(0, 5)
numero = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
time.sleep(2)
if numero == numeroPensado:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no {} e não no {}!'.format(numeroPensado, numero))
