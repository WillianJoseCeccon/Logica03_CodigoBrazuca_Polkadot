
#Atividade 6: Contagem de Vogais
#Solicitação: Crie um programa que peça uma frase ao usuário e conte quantas vogais (a, e, i, o,u) ela contém.

def contar_vogais(frase):
    vogais = "aeiouAEIOU"  # Conjunto de vogais, incluindo maiúsculas e minúsculas
    contador = 0

    # Percorre cada letra da frase
    for letra in frase:
        if letra in vogais:
            contador += 1

    return contador

# Solicita uma frase ao usuário
frase = input("Digite uma frase: ")

# Conta o número de vogais
numero_de_vogais = contar_vogais(frase)

# Exibe o resultado
print(f"A frase contém {numero_de_vogais} vogais.")