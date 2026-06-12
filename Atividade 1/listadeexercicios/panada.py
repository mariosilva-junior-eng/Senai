import time

print("="*50)
print("SISTEMA DE AUTOMAÇÃO DE IRRIGAÇÃO - GRUPO 5")
print("Vanessa Barp | Mario Junior | Anna dos Santos")
print("="*50)


umidade_atual = 15.0 
umidade_ideal = 40.0  
incremento = 5.0      

if umidade_atual >= umidade_ideal:
    print("Irrigação não necessária.")
else:
    print(f"Umidade inicial: {umidade_atual}%")
    print("--- INICIANDO REGA ---\n")

    while umidade_atual < umidade_ideal:

        umidade_atual += incremento
    
        if umidade_atual > umidade_ideal:
            umidade_atual = umidade_ideal

        print(f"Irrigador ligado... Umidade em {umidade_atual}%")
        
        time.sleep(0.5)

    print("\n" + "-"*40)
    print(f"Irrigação Concluída. Solo no nível ideal de {umidade_atual}%")
    print("Nível ideal atingido.")
    print("-"*40)