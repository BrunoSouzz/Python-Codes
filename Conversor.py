#Inico do conversor de moedas
#Importando a biblioteca
import os
#Definindo a função
def converter_moeda(valor, taxa_conversao):
    return valor * taxa_conversao
#Iniciando o loop
while True:
    #Limpa a tela
    os.system('cls' if os.name == 'nt' else 'clear')
    #Solicita o valor em reais
    valor_reais = float(input("Digite o valor em reais (ou 'sair' para encerrar o programa): "))
    #Verifica se o usuário deseja sair
    if valor_reais == 'sair':
        break
    #Solicita a taxa de conversão
    taxa_conversao = float(input("Digite a taxa de conversão: "))
    #Chama a função de conversão
    valor_convertido = converter_moeda(valor_reais, taxa_conversao)
    #Exibe o resultado
    print(f"Valor convertido: {valor_convertido}")