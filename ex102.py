def factorial(number, show=False):
    """

    :param number: Number to calculate its factorial
    :param show: (optional) Shows the calculation if show=True
    :return: the factorial result of the given number
    """
    f = 1
    for n in range(number, 0, -1):
        f *= n
        if show == 1 and n >= 2:
            print(f'{n} x ', end='')
        if show == 1 and n == 1:
            print(f'{n} = ', end='')
    return f


print(factorial(5))
help(factorial)