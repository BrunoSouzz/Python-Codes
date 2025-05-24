#Inicio do programa do relogio digital
#importando as bibliotecas necessárias
import tkinter as tk
import time
import os
#definindo a função que atualiza o relogio
def atualizar_relogio():
    #obtem o tempo atual
    tempo_atual = time.strftime("%H:%M:%S")
    #atualiza o label com o tempo atual
    relogio_label.config(text=tempo_atual)
    #chama a função novamente após 1000ms (1 segundo)
    relogio_label.after(1000, atualizar_relogio)

#Criando a janela principal
janela = tk.Tk()
janela.title("Relógio Digital")

#Criando o label que exibirá o horário
relogio_label = tk.Label(janela, font=("Helvetica", 48))
relogio_label.pack()

#Iniciando a atualização do relógio
atualizar_relogio()

#Iniciando o loop da interface gráfica
janela.mainloop()
#Fim do programa