n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
p = n1 ** n2
print('A soma é {}, a multiplicação é {}, a divisão é {}'.format(s,m,d), end=' ')
print('Divisão inteira é {}, potencia{}'.format(di,p))