import time

tempo = 10

for i in range(tempo, 0, -1):
    print(f"Tempo restante: {i} segundos")
    time.sleep(1)

print("Resfriamento concluído. Pode abrir a prensa.")