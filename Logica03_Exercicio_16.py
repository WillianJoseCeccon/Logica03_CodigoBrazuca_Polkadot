#Atividade 16: Inversão de String
#Solicitação: Crie um programa que peça uma string ao usuário e a exiba invertida

def inverter_string_loop(s):
    string_invertida = ""
    for caractere in s:
        string_invertida = caractere + string_invertida
    return string_invertida

# Solicita a string ao usuário
entrada = input("Digite uma string: ")

# Inverte a string
string_invertida = inverter_string_loop(entrada)

# Exibe a string invertida
print(f"A string invertida é: {string_invertida}")
