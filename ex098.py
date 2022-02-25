from time import sleep


def counter(*number):
    for n in range(*number):
        sleep(0.5)
        print(f'{n}', end=' ')
    print()
    print('=-' * 30)


print(f'Counting 1 to 10, 1 by 1.')
counter(0, 11, 1)
print('Counting 10 to 0, 2 by 2.')
counter(10, -1, -2)
print('Now choose a range of numbers and at which pace you want to count.')
beg = int(input('First number: '))
end = int(input('Final number: '))
step = int(input('Pace: '))
while beg > end:
    if step < 0:
        break
    step = step - (step * 2)
    end -= 1
    if step == 0:
        step = -1
    break
if beg < end:
    end += 1
if step == 0:
    step = 1

counter(beg, end, step)
