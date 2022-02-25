num = int(input('Até qual posição deseja ver a sequência de fibonacci? '))
seq = 0
add = 1
print('{}, {}, '.format(seq, add), end='')
parar = 3


while parar <= num:
    res = seq + add
    print('{}, '.format(res), end='')
    seq = add
    add = res
    parar += 1

print('FIM')
