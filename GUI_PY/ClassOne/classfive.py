# bilbioteca grafica do python 
import tkinter as tkin

def new():
    # apaga uma quantidade de caracteris que pode ser definidos o inicio e até onde ele que pagar"
    # delete(linha(float), até onde)
    text.delete(1.0, "end")

def save():
    # receber uma quantidade de caracteris que pode ser definidos com inicio e até onde ele que pagar"
    # get(linha(float), até onde)
    text_on_doc = text.get(1.0, "end")
    with open("notepad.txt", "w") as file:
        file.write(text_on_doc)


def open_file():
    read_doc = ""
    with open("notepad.txt", "r") as file:
        read_doc = file.read()
    # insert inseri uma quandiddade de valor  presente no seu conteudo e pode ser definiod o inicio
    # insert(linha de inicio(float), "string para o que deseja inserir")
    text.insert(1.0, read_doc)

#  configuração da janela 
window = tkin.Tk()
window.title("NOTEPAD")
window.geometry("760x500")

# adicionando campo de texto a janela
text = tkin.Text(window, font = "Arial 19 bold", width= 760, height = 500)

# pack() inseri o elemento na janela ou elemento atribuido a ele
text.pack()

# criando o menu principal 
menu = tkin.Menu(window)


# criando o menu segundario e vai dentro das opções do menu principal 
file = tkin.Menu(menu, tearoff = 0)


# adicionando os comandos que apareceram no menu segunda - File

file.add_command(label = "New File", command = new)
file.add_command(label = "Open", command = open_file)
file.add_command(label = "Save", command = save)
file.add_command(label = "Exit", command = window.quit)

menu.add_cascade(label = "Files", menu = file)

# configurnado a janela para receber o menu
# config - metodo que permite  implementar configurações a janela
window.config(menu= menu)

window.mainloop()