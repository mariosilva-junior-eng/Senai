cateto1 = float(input("Digite o valor do primeiro cateto: "))
cateto2 = float(input("Digite o valor do segundo cateto: "))

# Teorema de Pitágoras: a² + b² = c²
hipotenusa = (cateto1**2 + cateto2**2) ** 0.5

print(f"O valor da hipotenusa é: {hipotenusa:.2f}")