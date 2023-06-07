#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua area e a quantidade datinta necessaria para pinta-lá, sabendo que cada litro da tinta, pinta uma area de 2 metros quadrado.

altura = float(input("Qual a altura: "))
largura = float(input("Qual a sua largura: "))

area = altura * largura
tinta = area / 2

print("A area de parede é de {} metros quadrados".format(area))
print("Você precisará de {} litros de tinta para pintar a parede".format(tinta))