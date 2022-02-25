import math
n1 = float(input('Digite o valor do cateto oposto: '))
n2 = float(input('Digite o valor do cateto adjacente: '))
h = math.hypot(n1, n2)
print('a hipotenusa vai medir {:.2f}'.format(h))