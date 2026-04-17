
while True:
    peso_prato = float(input("digite o peso do prato pelo cliente (em quilos)")) 
    if peso_prato >=0:
        break
    print("valor invalido")

valor_a_pagar = peso_prato * 12.0
print ("o valor a pagar é de R$: ", valor_a_pagar)    