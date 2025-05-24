#inicio do programa de gerar senhas
import random
import string

def gerar_senha(tamanho=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for i in range(tamanho))
    return senha

# Solicitar o tamanho da senha ao usuário
tamanho = int(input("Digite o tamanho da senha desejada: "))
#Definir tamanho padrão
if tamanho < 6:
    print("O tamanho mínimo recomendado é 6 caracteres. Ajustando para 12.")
    tamanho = 12
    #Tamanho não pode ser menor que 6
# Gerar a senha
senha = gerar_senha(tamanho)
# Exibir a senha gerada
print("Senha gerada:", senha)
# Fim do programa de gerar senhas