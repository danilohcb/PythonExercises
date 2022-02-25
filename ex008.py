n = float(input('Digite uma distância em metros: '))
print('a medida de {} corresponde a: \n{}km \n{}hm \n{}dam \n{:.0f}dm \n{:.0f}cm \n{:.0f}mm'.format(n, n/1000, n/100, n/10, n*10, n*100, n*1000))
