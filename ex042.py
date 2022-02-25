print('-=-' * 15)
print('ANALISADOR DE TRIÂNGULOS!')
print('-=-' * 15)
lado1 = float(input('Primeiro lado: '))
lado2 = float(input('Segundo lado: '))
lado3 = float(input('Terceiro lado: '))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print('Os segmentos acima PODEM formar um triângulo ', end='')
    if lado1 == lado2 == lado3:
        print('EQUILATERO')
    elif lado1 == lado2 != lado3 or lado1 != lado2 == lado3 or lado1 != lado3 == lado2 or lado1 == lado3 != lado2:
        print('ISOCELES')
    elif lado1 != lado2 != lado3:
        print('ESCALENO')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo!')
