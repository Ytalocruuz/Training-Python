leia = input("Digite algo")

print(type(leia))
print("Só tem espaço: ", leia.isspace())
print("è um número", leia.isnumeric())
print("é alfabetico: ", leia.isalpha())
print("é alfanumerico: " , leia.isalnum())
print("está em maiusculas: ", leia.isupper())
print("está em minusculas: ", leia.islower())