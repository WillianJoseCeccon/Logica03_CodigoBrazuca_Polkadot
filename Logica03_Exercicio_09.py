#Atividade 9: Ordenação de Números
#Solicitação: Crie um programa que leia três números diferentes e os imprima em ordem crescente


def ordenar_numeros(a, b, c):
    if a > b:
        a, b = b, a
    if a > c:
        a, c = c, a
    if b > c:
        b, c = c, b
    return a, b, c

# Solicita três números diferentes ao usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# Ordena os números
num1, num2, num3 = ordenar_numeros(num1, num2, num3)

# Exibe os números em ordem crescente
print(f"Os números em ordem crescente são: {num1}, {num2}, {num3}")
