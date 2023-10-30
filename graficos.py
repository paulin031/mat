import math
import numpy as np
import matplotlib.pyplot as plt

# Função para calcular seno, cosseno e tangente de um ângulo em graus
def calcular_trigonometria(angulo_graus):
    angulo_radianos = math.radians(angulo_graus)
    seno = math.sin(angulo_radianos)
    cosseno = math.cos(angulo_radianos)
    tangente = math.tan(angulo_radianos)
    return seno, cosseno, tangente

# Função para calcular a distância entre dois pontos no plano cartesiano
def calcular_distancia_entre_pontos(x1, y1, x2, y2):
    distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distancia

# Função para criar gráficos das funções trigonométricas
def criar_grafico_trigonometria():
    angulos = np.linspace(0, 360, 360)  # Valores de ângulo de 0 a 360 graus
    seno, cosseno, tangente = [], [], []

    for angulo in angulos:
        s, c, t = calcular_trigonometria(angulo)
        seno.append(s)
        cosseno.append(c)
        tangente.append(t)

    plt.figure(figsize=(10, 6))
    plt.plot(angulos, seno, label='Seno')
    plt.plot(angulos, cosseno, label='Cosseno')
    plt.plot(angulos, tangente, label='Tangente')
    plt.xlabel('Ângulo (graus)')
    plt.ylabel('Valor')
    plt.legend()
    plt.title('Funções Trigonométricas')

# Função para criar gráfico de dois pontos e a linha que os conecta
def criar_grafico_posicao_pontos(x1, y1, x2, y2):
    plt.figure(figsize=(6, 6))
    plt.plot([x1, x2], [y1, y2], marker='o', linestyle='-', markersize=8)
    plt.xlabel('Eixo X')
    plt.ylabel('Eixo Y')
    plt.title('Posição Relativa de Dois Pontos')

# Função principal
def main():
    criar_grafico_trigonometria()
    plt.show()

    x1, y1 = 2, 3
    x2, y2 = 7, 8
    criar_grafico_posicao_pontos(x1, y1, x2, y2)
    plt.show()

    print("Exemplos de cálculos:")
    print("Distância entre os pontos (2, 3) e (7, 8):", calcular_distancia_entre_pontos(x1, y1, x2, y2))

if __name__ == "__main__":
    main()
