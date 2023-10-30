import math

def calcular_trigonometria():
    print("Escolha a operação de trigonometria:")
    print("1. Seno")
    print("2. Cosseno")
    print("3. Tangente")
    escolha = int(input("Digite o número da operação desejada: "))

    if escolha in (1, 2, 3):
        angulo_graus = float(input("Digite o valor do ângulo em graus: "))
        angulo_radianos = math.radians(angulo_graus)

        if escolha == 1:
            resultado = math.sin(angulo_radianos)
            print(f"Seno de {angulo_graus} graus é: {resultado}")
        elif escolha == 2:
            resultado = math.cos(angulo_radianos)
            print(f"Cosseno de {angulo_graus} graus é: {resultado}")
        elif escolha == 3:
            if math.cos(angulo_radianos) != 0:
                resultado = math.tan(angulo_radianos)
                print(f"Tangente de {angulo_graus} graus é: {resultado}")
            else:
                print("A tangente é indefinida (cosseno = 0).")
    else:
        print("Escolha de operação inválida.")

def calcular_area_triangulo():
    base = float(input("Digite o valor da base do triângulo: "))
    altura = float(input("Digite o valor da altura do triângulo: "))
    area = 0.5 * base * altura
    print(f"A área do triângulo é: {area}")

def determinar_posicao():
    x1 = float(input("Digite a coordenada x do primeiro ponto: "))
    y1 = float(input("Digite a coordenada y do primeiro ponto: "))
    x2 = float(input("Digite a coordenada x do segundo ponto: "))
    y2 = float(input("Digite a coordenada y do segundo ponto: "))

    if x1 == x2 and y1 == y2:
        print("Os pontos coincidem.")
    elif x1 == x2:
        print("Os pontos estão alinhados verticalmente.")
    elif y1 == y2:
        print("Os pontos estão alinhados horizontalmente.")
    else:
        print("Os pontos não estão alinhados.")

while True:
    print("\nEscolha uma opção:")
    print("1. Cálculos de Trigonometria")
    print("2. Cálculo de Área de Triângulo")
    print("3. Determinar a Posição Relativa de Pontos")
    print("4. Sair")

    opcao = int(input("Digite o número da opção desejada: "))

    if opcao == 1:
        calcular_trigonometria()
    elif opcao == 2:
        calcular_area_triangulo()
    elif opcao == 3:
        determinar_posicao()
    elif opcao == 4:
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")
