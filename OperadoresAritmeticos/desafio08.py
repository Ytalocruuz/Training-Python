#Escreva um progrma que leia um valor em metros e exiba convertido em centimetros e milimetros. 

metros  = float(input('Digite um valor em metros: '))

c = metros * 100
m = metros * 1000

print('Valor informado: {}, em centimetros {}, em milimetros: {}'.format(metros, c,m))