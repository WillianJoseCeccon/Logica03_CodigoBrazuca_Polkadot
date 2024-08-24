#Atividade 11: Cálculo de Área de Círculo
#Solicitação: Desenvolva um programa que calcule a área de um círculo a partir do raio fornecido pelo usuário.

import math

def calcular_area_circulo(raio):
    # Fórmula da área do círculo: A = πr²
    area = math.pi * (raio ** 2)
    return area

# Solicita o raio do círculo ao usuário
raio = float(input("Digite o raio do círculo: "))

# Calcula a área do círculo
area = calcular_area_circulo(raio)

# Exibe o resultado
print(f"A área do círculo com raio {raio} é {area:.2f}.")
