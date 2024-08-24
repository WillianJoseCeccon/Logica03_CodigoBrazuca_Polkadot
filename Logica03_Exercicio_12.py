#Atividade 12: Jogo de Adivinhação
#Solicitação: Crie um jogo onde o programa escolhe um número aleatório entre 1 e 100, e o usuário deve adivinhar qual é o número.

import random

def jogo_adivinhacao():
    # Gera um número aleatório entre 1 e 100
    numero_secreto = random.randint(1, 100)
    tentativas = 0

    print("Bem-vindo ao jogo de adivinhação!")
    print("Eu escolhi um número entre 1 e 100. Tente adivinhar qual é!")

    while True:
        try:
            # Solicita um palpite ao usuário
            palpite = int(input("Digite seu palpite: "))
            tentativas += 1

            # Verifica se o palpite está correto
            if palpite < numero_secreto:
                print("O número secreto é maior que o seu palpite.")
            elif palpite > numero_secreto:
                print("O número secreto é menor que o seu palpite.")
            else:
                print(f"Parabéns! Você acertou o número secreto {numero_secreto} em {tentativas} tentativas.")
                break

        except ValueError:
            print("Por favor, insira um número inteiro válido.")

# Inicia o jogo
jogo_adivinhacao()