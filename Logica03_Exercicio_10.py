#Atividade 10: Números Pares e Ímpares
#Solicitação: Escreva um programa que peça ao usuário um número inteiro e informe se ele é par ou ímpar


def verificar_paridade(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"

# Solicita um número inteiro ao usuário
numero = int(input("Digite um número inteiro: "))

# Verifica a paridade
paridade = verificar_paridade(numero)

# Exibe o resultado
print(f"O número {numero} é {paridade}.")