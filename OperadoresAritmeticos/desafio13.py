#Faça um algoritmo que leia o salario de um funcionario e mostre seu novo salário com 15% de aumento

salario = float(input("Insira seu sálario: R$"))

novoSalario = salario +(salario * 15 / 100)

print("Valor atualizado: R${}".format(novoSalario))

