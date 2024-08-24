
#Atividade 3: Cálculo de IMC
#Solicitação: Escreva um programa que peça o peso e a altura de uma pessoa e calcule seu Índice de Massa Corporal (IMC).

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

# Solicita o peso e a altura ao usuário
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

# Calcula o IMC
imc = calcular_imc(peso, altura)

# Exibe o resultado com duas casas decimais
print(f"Seu Índice de Massa Corporal (IMC) é {imc:.2f}.")