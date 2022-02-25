casa = float(input('Digite o valor da casa: R$'))
salario = float(input('Informe seu salário: R$'))
anos = int(input('Em quantos anos deseja pagar? '))
parcela = casa / (anos * 12)

print('Para pagar uma casa de R${:.2f} em {} anos, o valor das prestações serão de R${:.2f} por mês. '.format(casa, anos, parcela))

if parcela > (salario * 0.30):
    print('Empréstimo negado!')
elif parcela <= (salario * 0.30):
    print('Empréstimo concedido!')
