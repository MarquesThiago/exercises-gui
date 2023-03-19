# bilbioteca grafica do python 
import tkinter as tkin

#  configuração da janela 
window = tkin.Tk()
window.title("NOTEPAD")
window.geometry("760x500")

# criando o menu principal 
menu = tkin.Menu(window)


# criando o menu segundario e vai dentro das opções do menu principal 
file = tkin.Menu(menu, tearoff = 0)


# adicionando os comandos que apareceram no menu segunda - File
# add_command(label = "nome", command = funçaõ) é um atributo que adiciona um comando para realizar determinada operação ele recebe label com o nome e command para 
# inserir a função

file.add_command(label = "New File", command = None)
file.add_command(label = "SAve", command = None)


# window.quit = fuçõa incluida no tkinter que fecja a janela
file.add_command(label = "Exit", command = window.quit)

menu.add_cascade(label = "Files", menu = file)

# configurnado a janela para receber o menu
# config - metodo que permite  implementar configurações a janela
window.config(menu= menu)

window.mainloop()