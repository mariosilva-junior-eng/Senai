qtd_sanduiche = int(input("Digite a quantidade de sanduiches a fazer: "))
peso_queijo = 50
peso_presunto = 50
peso_carne = 100

total_queijo = (qtd_sanduiche * 2 * peso_queijo)/1000
total_presunto = (qtd_sanduiche * 1 * peso_presunto)/1000
total_carne = (qtd_sanduiche * 1 * peso_carne)/1000

print(f"Para produzir {qtd_sanduiche} sanduiches, você precisa de: ")
print(f"--Queijo: {total_queijo} kg")
print(f"--Presuntoo: {total_presunto} kg")
print(f"--Carne: {total_carne} kg")