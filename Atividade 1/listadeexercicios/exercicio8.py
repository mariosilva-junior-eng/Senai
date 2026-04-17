nota_1 = float(input("Insira O Valor Da Primeira Nota: "))
nota_2 = float(input("Insira O Valor Da Segunda Nota: "))
nota_3 = float(input("Insira O Valor Da Terceira Nota: "))

# nota 1 possui peso 1, nota 2, 2, nota 3, 3.

media_ponderada = (nota_1 + nota_2 * 2 + nota_3 * 3) / 6

print(f"A sua média ponderada é igual a: ", media_ponderada)