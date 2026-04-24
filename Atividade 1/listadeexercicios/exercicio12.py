salario = float(input("Digite seu salario atual: "))
x = salario * 0.15
aumento = salario + x
imposto = aumento * 0.08
salariofinal = aumento - imposto
print("O salario sem almento era: ", salario)
print("O salario com almento ficou: ", salario)
print("O salario final ficou: ", salariofinal)
