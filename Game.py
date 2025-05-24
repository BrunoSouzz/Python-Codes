#iniciar programa de jogo de dados
import random

def jogar_dados():
    return random.randint(1, 6)
def jogar():
    print("Bem-vindo ao jogo de dados!")
    print("Pressione 'Enter' para jogar os dados ou 'q' para sair.")
    while True:
        comando = input()
        if comando == 'q':
            break
        elif comando == '':
            resultado = jogar_dados()
            print(f"Você rolou um {resultado}!")
        else:
            print("Comando inválido. Pressione 'Enter' para jogar ou 'q' para sair.")