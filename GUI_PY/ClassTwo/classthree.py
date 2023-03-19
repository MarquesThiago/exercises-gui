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

        # Entreda de valores        
        self.entry = thin.Entry(self.window, font = "Verdana 20 bold", bg= self.__bg_color, fg = self.__color, width  = 18)
        self.entry.pack()

       

        self.frame = thin.Frame(self.window)
        self.frame.pack()

         # Botoes numericos 
         # lambda e o parametro que diz para que esse comando não seja aplicado assim que o codigo  
        # iniciar so quando houver algum evento no  botão isso só e necessario quando temos a função com parametros 
        self.button_1 = self._create_button("1", command = lambda: self._touch("1"))
        self.button_2 = self._create_button("2", command = lambda: self._touch("2"))
        self.button_3 = self._create_button("3", command = lambda: self._touch("3"))
        self.button_4 = self._create_button("4", command = lambda: self._touch("4"))
        self.button_5 = self._create_button("5", command = lambda: self._touch("5"))
        self.button_6 = self._create_button("6", command = lambda: self._touch("6"))
        self.button_7 = self._create_button("7", command = lambda: self._touch("7"))
        self.button_8 = self._create_button("8", command = lambda: self._touch("8"))
        self.button_9 = self._create_button("9", command = lambda: self._touch("9"))
        self.button_0 = self._create_button("0", command = lambda: self._touch("0"))
        
        self.button_plus = self._create_button("+" , command = lambda: self._touch("+"))
        self.button_sub = self._create_button("-", command = lambda: self._touch("-") )
        self.button_mul = self._create_button("*", command = lambda: self._touch("*"))
        self.button_div = self._create_button("/", command = lambda: self._touch("/"))
        self.button_eq = self._create_button("=", w = 10, command = self.total)
        self.button_clear = self._create_button("C", command = self.clean)
        self.button_remove = self._create_button("<-", w = 15, command = self.remove)

        
        self.button_clear.grid(row = 0, column = 0)
        self.button_remove.grid(row = 0, column = 1, columnspan = 3)


        self.button_1.grid(row = 3, column = 0)
        self.button_2.grid(row = 3, column = 1)
        self.button_3.grid(row = 3, column = 2)
        self.button_div.grid(row = 3 , column = 3)


        self.button_4.grid(row = 2, column = 0)
        self.button_5.grid(row = 2, column = 1)
        self.button_6.grid(row = 2, column = 2)
        self.button_mul.grid(row = 2, column = 3)

        self.button_7.grid(row = 1, column = 0)
        self.button_8.grid(row = 1, column = 1)
        self.button_9.grid(row = 1, column = 2)
        self.button_sub.grid(row = 1, column = 3)

        self.button_0.grid(row = 4, column = 0)
        self.button_eq.grid(row = 4, column = 1, columnspan = 2)
        self.button_plus.grid(row = 4, column = 3)

        self.window.mainloop()

    def _create_button(self, text, command = None, w = 5,h = 3 ):
        button = thin.Button(self.frame, 
                            bg = "Orange", 
                            text = text, 
                            font= "Arial 20 bold", 
                            width = w, 
                            height = h, 
        
                            command = command,
                            padx = 0 )
        return button

    def _touch(self, action):
        # insert e uma função do Entru para inserir valores neste estamos pegando o 
        # final end e vamos adicionar o que tiver em action
        self.entry.insert(thin.END, action)
    
    def clean(self):
        # delete remove os caracteres de um ponto ao outro
        self.entry.delete(0, thin.END)


    def remove(self):
        # a get e uma função que returna tudo o  ques esta inserdo no nossa entrada
        len_entry =len(self.entry.get())
        self.entry.delete(len_entry-1, thin.END)

    def total(self):
        
        str_entry = self.entry.get()
        total = eval(str_entry)
        self.clean()
        self._touch(f"{total}")

Calc()