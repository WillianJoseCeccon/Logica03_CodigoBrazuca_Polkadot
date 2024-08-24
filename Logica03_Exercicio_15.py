#Atividade 15: Soma dos N primeiros Números
#Solicitação: Escreva um programa que peça ao usuário um número n e calcule a soma dos primeiros n números naturais.

def soma_n_primeiros_numeros(n):
    soma = 0
    for i in range(1, n + 1):
        soma += i
    return soma

def obter_numero_valido(prompt):
    while True:
        try:
            numero = int(input(prompt))
            if numero < 1:
                print("Por favor, insira um número natural positivo.")
            else:
                return numero
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro válido.")

# Solicita o número n ao usuário
n = obter_numero_valido("Digite um número natural n: ")

# Calcula a soma dos primeiros n números naturais
resultado = soma_n_primeiros_numeros(n)

# Exibe o resultado
print(f"A soma dos primeiros {n} números naturais é {resultado}.")
