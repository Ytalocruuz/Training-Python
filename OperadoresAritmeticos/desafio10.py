# Crie um programa que leia quanto dinheiro uma pessoa tem na  carteira e mostre quantos dólares ela pode comprar. 

BR = float(input("Valor: R$"))

DL = BR / 4.92

print("Valor em real: R${:.2f}".format(BR))
print("Valor em dolar: US${:.2f}".format(DL))