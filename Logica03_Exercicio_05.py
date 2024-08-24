
#Atividade 5: Tabuada
#Solicitação: Escreva um programa que exiba a tabuada de um número fornecido pelo usuário


def exibir_tabuada(numero):
    print(f"Tabuada do {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

# Solicita um número ao usuário
numero = int(input("Digite um número para ver sua tabuada: "))

# Exibe a tabuada
exibir_tabuada(numero)