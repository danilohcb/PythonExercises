import math
ang = float(input('Digite o ângulo que você deseja: '))
print('O ângulo de {} tem o SENO de: {:.2f}'.format(ang, math.sin(math.radians(ang))))
print('O ângulo de {} tem o COSSENO de: {:.2f}'.format(ang, math.cos(math.radians(ang))))
print('O ângulo de {} tem a TANGENTE de: {:.2f}'.format(ang, math.tan(math.radians(ang))))
