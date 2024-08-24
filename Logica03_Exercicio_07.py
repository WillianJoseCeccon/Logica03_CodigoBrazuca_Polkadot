#Atividade 7: Média de Notas
#Solicitação: Desenvolva um programa que calcule a média de várias notas inseridas pelo usuário. O programa deve parar de pedir notas quando o usuário digitar -1.



def calcular_media():
    soma_notas = 0
    contador_notas = 0

    while True:
        nota = float(input("Digite uma nota (ou -1 para finalizar): "))
        
        if nota == -1:
            break
        
        soma_notas += nota
        contador_notas += 1

    if contador_notas > 0:
        media = soma_notas / contador_notas
        print(f"A média das {contador_notas} notas inseridas é {media:.2f}.")
    else:
        print("Nenhuma nota válida foi inserida.")

# Executa o cálculo da média
calcular_media()