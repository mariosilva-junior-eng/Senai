
dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês (1-12): "))

dias_passados = ((mes - 1) * 30) + dia

print(f"Desde o início do ano, passaram-se {dias_passados} dias.")