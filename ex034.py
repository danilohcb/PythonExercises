salario = float(input('Quanto é o seu salário? R$'))
if salario <= 1250:
    aumento = salario * 0.15 + salario
else:
    aumento = salario * 0.1 + salario

print('O seu salário recebendo o devido aumento é de R${:.2f}'.format(aumento))