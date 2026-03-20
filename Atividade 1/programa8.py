nome = input("digite seu nome: ")
idade = int(input("digite sua idade: "))
while True:
    if idade > 120 or idade < 0:
        print("idade invalida! por favor, digite um valor menor ou igual a 120")
        idade = int(input("digite sua idade: "))
    else:
        break
dias_de_vida = idade * 365
print(f"olá {nome}, você já viveu cerca de:  {dias_de_vida}")