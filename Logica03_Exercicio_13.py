#Atividade 13: Soma de Números Pares
#Solicitação: Escreva um programa que calcule a soma de todos os números pares entre 1 e 100.


def soma_numeros_pares(inicio, fim):
    soma = 0
    for numero in range(inicio, fim + 1):
        if numero % 2 == 0:
            soma += numero
    return soma

# Define o intervalo de 1 a 100
inicio = 1
fim = 100

# Calcula a soma dos números pares
resultado = soma_numeros_pares(inicio, fim)

# Exibe o resultado
print(f"A soma de todos os números pares entre {inicio} e {fim} é {resultado}.")