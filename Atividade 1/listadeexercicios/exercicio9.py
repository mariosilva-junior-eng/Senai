quantidade_p = int(input("Insira A Quantidade De Camisas De Pequenas: "))
quantidade_m = int(input("Insira A Quantidade De Camisas De Médias: "))
quantidade_g = int(input("Insira A Quantidade De Camisas De Grandes: "))

valor_final = (quantidade_p * 10) + (quantidade_m * 12) + (quantidade_g * 15)

print(f"O Valor Final É: ", valor_final)