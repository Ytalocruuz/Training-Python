# Escreva um programa que pergunte a quantidade da KM percorrido por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado. 

dias = int(input("Quantos dias alugados: "))
km = float(input("Qauntos KM rodados: "))
pago = (dias * 60) + (km * 0.15)

print("O total a pagar é de  R${}".format(pago))
