from time import sleep


def biggest(*number):
    print('~~' * 30)
    print(f'{"Values writen were:":^60}')
    for n in number:
        sleep(0.5)
        print(f'     {n:^5} ', end='')
    print()
    print('~~' * 30)
    print(f'{len(number)} numbers in total.')
    print('The biggest number was: ', end='')
    print(max(number))


biggest(20, 5, 7, 10, 13, 14)
