#Atividade 18: Contagem de Palavras
#Solicitação: Desenvolva um programa que conte quantas palavras há em uma frase fornecida pelo usuário


def contar_palavras(frase):
    palavras = frase.split()
    return len(palavras)

# Solicita a frase ao usuário
frase = input("Digite uma frase: ")

# Conta o número de palavras na frase
numero_palavras = contar_palavras(frase)

# Exibe o resultado
print(f"A frase contém {numero_palavras} palavras.")
