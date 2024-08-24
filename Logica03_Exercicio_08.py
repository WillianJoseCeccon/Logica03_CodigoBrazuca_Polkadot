#Atividade 8: Sequência de Fibonacci
#Solicitação: Escreva um programa que mostre os primeiros n números da sequência de Fibonacci, onde n é informado pelo usuário.

def gerar_fibonacci(n):
    fibonacci = []
    a, b = 0, 1
    for _ in range(n):
        fibonacci.append(a)
        a, b = b, a + b
    return fibonacci

# Solicita o número de termos ao usuário
n = int(input("Digite o número de termos da sequência de Fibonacci: "))

# Gera a sequência de Fibonacci
sequencia_fibonacci = gerar_fibonacci(n)

# Exibe a sequência
print(f"Os primeiros {n} números da sequência de Fibonacci são:")
print(sequencia_fibonacci)
