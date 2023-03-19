# bilbioteca grafica do python 
import tkinter as tkin

#  configuração da janela 
window = tkin.Tk()
window.title("NOTEPAD")
window.geometry("760x500")

# Menu(janela\objeto a qual esta incluido, tearoof = 0) - cria um objeto do tipo menu
# tearoff separa o menu e coloca numa janela separada 

menu = tkin.Menu(window, tearoff = 0)

# add_cascade - metodo que adiciona uma opção do tipo drop down ou cascade ao menu
menu.add_cascade(label = "New")

# configurnado a janela para receber o menu
# config - metodo que permite  implementar configurações a janela
window.config(menu= menu)

window.mainloop()