#Atividade 20: Análise de Lista de Números
#Solicitação: Escreva um programa que peça ao usuário uma lista de números e, ao final, exiba o maior, o menor, e a média dos números inseridos

def obter_lista_numeros():
    numeros = []
    while True:
        entrada = input("Digite um número (ou 'fim' para encerrar): ")
        if entrada.lower() == 'fim':
            break
        try:
            numero = float(entrada)
            numeros.append(numero)
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido ou 'fim' para encerrar.")
    return numeros

def analisar_lista(numeros):
    if not numeros:
        return None, None, None
    
    maior = max(numeros)
    menor = min(numeros)
    media = sum(numeros) / len(numeros)
    
    return maior, menor, media

# Obtém a lista de números do usuário
lista_numeros = obter_lista_numeros()

# Analisa a lista e obtém o maior, menor e a média
maior, menor, media = analisar_lista(lista_numeros)

# Exibe os resultados
if lista_numeros:
    print(f"O maior número é: {maior}")
    print(f"O menor número é: {menor}")
    print(f"A média dos números é: {media:.2f}")
else:
    print("Nenhum número foi inserido.")
