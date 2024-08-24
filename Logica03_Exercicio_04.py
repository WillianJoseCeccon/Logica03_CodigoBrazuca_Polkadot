#Atividade 4: Verificação de Palíndromo
#Solicitação: Crie um programa que verifique se uma palavra ou frase é um palíndromo


def eh_palindromo(texto):
    # Remove espaços e converte para minúsculas
    texto_limpo = ''.join(caractere.lower() for caractere in texto if caractere.isalnum())
    # Verifica se o texto limpo é igual ao seu reverso
    return texto_limpo == texto_limpo[::-1]


# Solicita uma palavra ou frase ao usuário
texto = input("Digite uma palavra ou frase: ")


# Verifica se é um palíndromo
if eh_palindromo(texto):
    print(f'"{texto}" é um palíndromo.')
else:
    print(f'"{texto}" não é um palíndromo.')
