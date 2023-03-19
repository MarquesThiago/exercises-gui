# bilbioteca grafica do python 
import tkinter 

# Tk cria um objedto da clase tk que é responsavel por ser intepretador do ambiente 
window = tkinter.Tk()

# title - atributo de nome da janela
window.title("NOTEPAD")

#minsize(width=, height=) - define o tamanho minimo para a janela
# window.minsize(width = 580, height = 500)

#geomtry("widthxheight") = propriedade de acesso a gemotria do objeto, tamanho, largura e posição, e outra forma de tambem
# adicionarmos o tamanho desejado da tabela entretando ela é redimensionavel e não assume o tamanho passado
# como uma restrição de tamanho como no caso do minsize e maxsize
window.geometry("760x500")

# mainloop - start a janela e como a rodar em loop.
window.mainloop()