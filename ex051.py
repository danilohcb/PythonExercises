termo = int(input('Informe o primeiro termo de uma PA: '))
razão = int(input('Agora informe a razão dessa PA: '))
limite = termo + (10 - 1) * razão

for num in range(termo, limite + razão, razão):
    print(num)
