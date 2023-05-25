# Faça um algoritmo que leia o preço de um produto e msotre seu novo preço, com 5% de desconto. 
precoOriginal = float(input("Digite o valor do produto: "))

precoComDesconto = precoOriginal - (precoOriginal  * 5 / 100) 

print("O valor com desconto: {}".format(precoComDesconto))



