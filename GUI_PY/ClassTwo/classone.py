from tkinter import Tk 
import tkinter as thin

class Calc():

    def __init__(self):
        self.window = Tk()
        self.__bg_color = '#213059'
        self.window.title("Calculator")
        # significa que não vai escolonar nem no eixo x e y 
        # se vocÊ colcoarr uma seja para x ou y esse eixo se torna escalonavel
        self.window.resizable(0,0)

        # alterando a cor do background da janela
        self.window.config(bg = self.__bg_color)

        # import: passamos para a nossa janela um frame e como a nossa janela não tem tamanho predefinido
        # ela se ajusta aos elementos dentro dela e como e esse não for passadp tamanho para o fram
        # e como se a tabela ja nem existisse 
        # alem disso o backgroun tem a cor por padrão de cinza para os frames 
        self.frame = thin.Frame(self.window, width = 360, height = 350, bg = self.__bg_color)

        self.window.mainloop()


Calc()