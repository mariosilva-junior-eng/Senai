"dias_trabalhados = int(input("Digite o número de dias trabalhados: "))

anos = dias_trabalhados // 365
meses = (dias_trabalhados % 365) // 30
dias = (dias_trabalhados % 365) % 30


print(f"{dias_trabalhados} dias equivalem a {anos} anos, {meses} meses e {dias} dias.")"