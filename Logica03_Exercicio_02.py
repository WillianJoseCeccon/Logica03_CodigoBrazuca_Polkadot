
#Atividade 2: Conversão de Temperaturas
#Solicitação: Crie um programa que converta uma temperatura dada em Celsius para Fahrenheit e Kelvin.


def converter_temperatura(celsius):
    fahrenheit = (celsius * 9/5) + 32
    kelvin = celsius + 273.15
    return fahrenheit, kelvin

# Solicita uma temperatura em Celsius ao usuário
celsius = float(input("Digite a temperatura em Celsius: "))

# Converte para Fahrenheit e Kelvin
fahrenheit, kelvin = converter_temperatura(celsius)

# Exibe os resultados
print(f"A temperatura de {celsius}°C corresponde a {fahrenheit}°F e {kelvin} K.")
