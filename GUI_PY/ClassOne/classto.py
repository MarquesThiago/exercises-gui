# bilbioteca grafica do python 
import tkinter as tkin

#  configuração da janela 
window = tkin.Tk()
window.title("NOTEPAD")
window.geometry("760x500")

# Text(janela/elemento que o vai receber, font = "font-family font-size type", lagura , altura) - cria um ovjeto do tipo text que implemente em uma janela uma area para inserção de text 
# adicionando campo de texto a janela
text = tkin.Text(window, font = "Arial 19 bold", width= 760, height = 500)

# pack() inseri o elemento na janela ou elemento atribuido a ele
text.pack()

# As funções como control + C ou Control + V entre outras não são necessarias criar configurações
# para implementa-las logo que ja são implementas pelo prorpio sistema operacional 


window.mainloop()