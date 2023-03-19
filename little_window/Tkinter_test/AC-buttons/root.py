from tkinter import *


root = Tk()

def clicked():
    label = Label(root, text = "Added text in your window" )
    label.pack()

#@params - state (DISABLED = o botão fica com o tom de acizentado como se estive desativo)
    # padx (number = que da um padding para left e right do botão)
    # pady (number = que da um padding para top e bottom do botão)
    # command (function = recebe uma função para ser executada toda vez que o botão e clicado, a 
    #   função não pode ter parenteses)
    # fg ("color" =  cor da fonte)
    # bg ("color" = cor de fundo )
    
button = Button(root, text = "CLick Me, Please", state = DISABLED, padx = 30, pady = 20 )
button2 = Button(root, text = "Add Text", padx = 30, pady = 20, command= clicked, fg = "white", bg= "#9999ff" )
button.pack()
button2.pack()



root.mainloop()