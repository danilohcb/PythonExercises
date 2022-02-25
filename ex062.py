termo = int(input('Informe o primeiro termo de uma PA: '))
razão = int(input('Agora informe a razão dessa PA: '))
limite = 0
cond = 10
while limite != cond:
    print(termo)
    termo += razão
    limite += 1
    if limite == cond:
        cond = int(input('Deseja mostar mais quantos termos? (Digite 0 para parar): '))
        if cond != 0:
            cond = limite + cond
        else:
            print('FIM')
            break
