numero = int(input("Digite um número de 0 a 10: "))

if numero >= 0 and numero <= 10:
    for i in range(0, 11):
        print(numero, "x", i, "=", numero * i)
else:
    print("Número inválido!")