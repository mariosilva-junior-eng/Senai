quant_pao = int(input("digite a quantidade de pao vendidos"))
quant_broa = int(input("digite a quantidade de broa vendidos"))

arrecadado = (quant_pao * 0.12) + (quant_broa * 1.50)
poupança = ( arrecadado * 0.10)

print("total de vendas de pao e broas foi: ",arrecadado)
print("quantidade e dinheiro que ira para poupança: ",poupança)