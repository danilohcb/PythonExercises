import random
vitorias = 0
cond = ''
while True:
    print('-=' * 40)
    num = int(input('Digite um número: '))
    escolha = str(input('Par ou Ímpar? (P/I): ')).lower().strip()[0]
    comp = random.randint(0, 10)
    res = num + comp
    if res % 2 == 0:
        cond = 'par'
    if res % 2 != 0:
        cond = 'ímpar'
    if res % 2 == 0 and escolha == 'p':
        print(f'\033[033mO computador jogou {comp}.\033[m')
        print(f'Você venceu! Deu {res} e é par. Vamos de novo!')
        vitorias += 1
    elif res % 2 != 0 and escolha == 'i':
        print(f'\033[033mO computador jogou {comp}.\033[m')
        print(f'Você venceu! Deu {res} e é ímpar. Vamos de novo!')
        vitorias += 1
    else:
        print(f'\033[033mO computador jogou {comp}.\033[m')
        print(f'Você perdeu! Deu {res}, é {cond}. Você ganhou {vitorias} vezes seguidas')
        break
