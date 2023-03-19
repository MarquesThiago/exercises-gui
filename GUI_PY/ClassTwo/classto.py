from tkinter import Tk 
import tkinter as thin

class Calc():

    def __init__(self):
        self.window = Tk()
        self.__bg_color = '#213059'
        self.__color = "white"
        self.window.title("Calculator")
        self.window.resizable(0,0)        
        self.window.config(bg = self.__bg_color)

        # Entry e um wiogdet de entrada de valores assim como o text so que menor 
        # width = cpntrola a quantidade de caracters maximo
    
        self.entry = thin.Entry(self.window, font = "Verdana 20 bold", bg= self.__bg_color, fg = self.__color)
        self.entry.pack()

        self.frame = thin.Frame(self.window)
        self.frame.pack()

        self.window.mainloop()


Calc()