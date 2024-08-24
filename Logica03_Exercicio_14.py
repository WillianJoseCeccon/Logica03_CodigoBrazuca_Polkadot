#Calculadora Simples
#Solicitação: Crie um programa que funcione como uma calculadora simples, pedindo ao usuário dois números e a operação que deseja realizar

def obter_numero_valido(prompt):
    while True:
        try:
            numero = float(input(prompt))
            return numero
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")

def obter_operador_valido():
    while True:
        operador = input("Digite a operação (+, -, *, /): ")
        if operador in ('+', '-', '*', '/'):
            return operador
        else:
            print("Caractere indesejado. Por favor, digite um dos seguintes operadores: +, -, *, /.")

def calculadora():
    # Solicita números válidos ao usuário
    num1 = obter_numero_valido("Digite o primeiro número: ")
    num2 = obter_numero_valido("Digite o segundo número: ")
    
    # Obtém um operador válido
    operador = obter_operador_valido()

    # Verifica e realiza a operação
    if operador == '+':
        resultado = num1 + num2
    elif operador == '-':
        resultado = num1 - num2
    elif operador == '*':
        resultado = num1 * num2
    elif operador == '/':
        if num2 != 0:
            resultado = num1 / num2
        else:
            return "Erro: Divisão por zero não é permitida."

    return f"O resultado de {num1} {operador} {num2} é {resultado}."

# Executa a calculadora
print(calculadora())
