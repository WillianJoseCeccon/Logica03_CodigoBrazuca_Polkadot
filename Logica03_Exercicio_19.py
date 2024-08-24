#Atividade 19: Média Ponderada
#Solicitação: Crie um programa que calcule a média ponderada de três notas fornecidas pelo usuário, considerando os pesos 2, 3 e 5

def calcular_media_ponderada(nota1, nota2, nota3):
    # Pesos das notas
    peso1 = 2
    peso2 = 3
    peso3 = 5
    
    # Calcula a média ponderada
    soma_ponderada = (nota1 * peso1) + (nota2 * peso2) + (nota3 * peso3)
    soma_pesos = peso1 + peso2 + peso3
    media_ponderada = soma_ponderada / soma_pesos
    
    return media_ponderada

def obter_nota_valida(prompt):
    while True:
        try:
            nota = float(input(prompt))
            if 0 <= nota <= 10:
                return nota
            else:
                print("Nota inválida. Por favor, insira um valor entre 0 e 10.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")

# Solicita as notas ao usuário
nota1 = obter_nota_valida("Digite a primeira nota (0 a 10): ")
nota2 = obter_nota_valida("Digite a segunda nota (0 a 10): ")
nota3 = obter_nota_valida("Digite a terceira nota (0 a 10): ")

# Calcula a média ponderada
media = calcular_media_ponderada(nota1, nota2, nota3)

# Exibe o resultado
print(f"A média ponderada das notas é: {media:.2f}")
