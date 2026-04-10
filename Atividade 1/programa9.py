contador = 1
soma = 0
while contador <= 5:
    salario = float(input(f"Digite o Salario do {contador} Funcionario: "))
    contador += 1
    soma += salario
media = soma / 5
print ("A media dos salarios dos 5 Funcionarios é: ", media)