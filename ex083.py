expressao = list()
expr = (str(input('Digite sua expressão matemática: ')))
for n in expr:
    if n == '(':
        expressao.append('(')
    elif n == ')':
        if len(expressao) > 0:
            expressao.pop()
        else:
            expressao.append(')')
            break

if len(expressao) == 0:
    print('Sua expressão é válida!')
else:
    print('Sua expressão está incorreta!')
