#Atividade 17: Verificação de Número Perfeito
#Solicitação: Escreva um programa que verifique se um número dado é um número perfeito.


def verificar_numero_perfeito(n):
    if n <= 0:
        return False
    
    soma_divisores = 0
    # Encontra todos os divisores próprios de n
    for i in range(1, n):
        if n % i == 0:
            soma_divisores += i
    
    # Verifica se a soma dos divisores é igual ao número
    return soma_divisores == n

def obter_numero_valido(prompt):
    while True:
        try:
            numero = int(input(prompt))
            if numero <= 0:
                print("Por favor, insira um número inteiro positivo.")
            else:
                return numero
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro válido.")

# Solicita o número ao usuário
numero = obter_numero_valido("Digite um número para verificar se é perfeito: ")

# Verifica se o número é perfeito
if verificar_numero_perfeito(numero):
    print(f"O número {numero} é um número perfeito.")
else:
    print(f"O número {numero} não é um número perfeito.")
