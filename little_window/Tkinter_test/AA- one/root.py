from tkinter import *

##
#@params - Tk cria um container para ser aplido;
root = Tk()

## Label cria uma label onde definimos onde vai ser adicionado e o testo 
text = Label(root, text = "Hello ladys and gentlemans")

##o pack joga o elemento para dentro do container
text.pack()

##mainloop deixa a interface rodando em loop
root.mainloop()


