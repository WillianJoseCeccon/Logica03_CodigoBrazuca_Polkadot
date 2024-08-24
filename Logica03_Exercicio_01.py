#Atividade 1: Calculando o Fatorial
#Solicitação: Escreva um programa que peça um número inteiro ao usuário e calcule o fatorial desse número.

def calcular_fatorial(numero):
    fatorial = 1
    while numero > 1:
        fatorial *= numero
        numero -= 1
    return fatorial

# Função para solicitar um número inteiro e positivo
def solicitar_numero():
    while True:
        try:
            numero = int(input("Digite um número inteiro positivo para calcular o fatorial: "))
            if numero >= 0:
                return numero
            else:
                print("Por favor, digite um número positivo.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

# Solicita um número ao usuário
numero = solicitar_numero()

# Calcula o fatorial
fatorial = calcular_fatorial(numero)

# Exibe o resultado
print(f"O fatorial de {numero} é {fatorial}.")
