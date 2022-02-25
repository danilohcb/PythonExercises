boletim = dict()
boletim['Nome'] = str(input('Nome do aluno: '))
boletim['Média'] = float(input(f'Média de {boletim["Nome"]}: '))
print('=-' * 30)
if boletim['Média'] >= 7:
    boletim['Situação'] = 'Aprovado'
elif 7 > boletim['Média'] >= 5:
    boletim['Situação'] = 'Recuperação'
else:
    boletim['Situação'] = 'Reprovado'

for v, k in boletim.items():
    print(f'{v} é igual a {k}')
