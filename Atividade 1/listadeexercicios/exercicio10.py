import math

def calcular_distancia(p1, p2):
    distancia = math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)
    return distancia

ponto_a = (1, 2)
ponto_b = (4, 6)

resultado = calcular_distancia(ponto_a, ponto_b)
print(f"A distância é: {resultado}")