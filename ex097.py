def write(text):
    border = (len(text) * 2)
    print('~' * border)
    print(f'{text.center(border)}')
    print('~' * border)


write('Anything')
write('It matches the size!')
write('Hello World')
