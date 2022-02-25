from random import randint
numbers = list()


def drawing():
    for n in range(0, 5):
        generate = randint(1, 100)
        numbers.append(generate)
    print(numbers)


def evenresult():
    result = 0
    for n in numbers:
        if n % 2 == 0:
            result += n
    print(result)


print('The 5 numbers generated were: ', end=' ')
drawing()
print()
print('And the sum of the even numbers is: ', end='')
evenresult()
