#Inicio do progama de tabuada
#Importando a biblioteca
import os
#Definindo a função
def tabuada():
    numero = int(input("Digite um número inteiro para ver sua tabuada: "))
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
#Iniciando o loop
while True:
    #Chama a função
    tabuada()
    #Pergunta se o usuário quer continuar
    continuar = input("Deseja ver a tabuada de outro número? (s/n): ")
    if continuar.lower() != 's':
        print("Programa encerrado.")
        break
    #Limpa a tela
    os.system('cls' if os.name == 'nt' else 'clear')
#Fim do programa