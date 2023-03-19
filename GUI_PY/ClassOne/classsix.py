# bilbioteca grafica do python 
import tkinter as tkin

def new():
    text.delete(1.0, "end")

def save():
    text_on_doc = text.get(1.0, "end")
    with open("notepad.txt", "w") as file:
        file.write(text_on_doc)


def open_file():
    read_doc = ""
    with open("notepad.txt", "r") as file:
        read_doc = file.read()
    new()
    text.insert(1.0, read_doc)

def update():
    font= spin_font_values.get()
    size = spin_size_values.get()
    text.config(font = f"{font} {size}")


window = tkin.Tk()
window.title("NOTEPAD")
window.geometry("760x500")
window.minsize(width=720, height = 480)

#frame: ele cria uma caixa dentro da janela para que você possa armazenar outros widgets 
#frame(in, height- opcional, wigdet - opcional) = in - aonde esta dentro se uma janela, de outro frame 
# bg aplica o cor ao backgroun do wigdet
frame = tkin.Frame(window, height= 30, bg = 'gray') 

#pack e um comando que empilha a os objetos dentro do uma janela ou frame, so colacando ele no centro 
# mas tambem pode receber por parametro o de prenchimento que defini em que eixo ele ira colocar os objetos
# fill= "X" pre diz que ele crescera infinitamente no eixo x 
# tambem temos o side que podemos colocar onde o nosso objeto vai esta posicionado right, left, center, top, bottom
# padx , pady adiciona uma espacamento entre um widget e outro
frame.pack(fill = "x")


# Label e uma widget que serve como argumento para  parametro texto 
text_font = tkin.Label(frame, text  = "Font: ")
text_font.pack(side = 'left')

# spinbox = é o com flexas de top e bottom 
# values é uma tuplas com todos os seus posiveis valores 
# tambem temos do from_ e o to que relativo de onde para onde por exemplo 0 a 10
spin_font_values = tkin.Spinbox(frame, values = ("Arial", "Times New Roman", "Verdana"))
spin_font_values.pack(side = "left") 

size_font = tkin.Label(frame, text  = "Size: ")
size_font.pack(side = 'left')

spin_size_values = tkin.Spinbox(frame, from_ = 1, to = 65 )
spin_size_values.pack(side = "left") 


#  ---------------------------------------------
#  | criando botão  para aplicar alterações     |
#  ----------------------------------------------

update_font = tkin.Button(frame, text= "Apply", command = update)
update_font.pack()



text = tkin.Text(window, font = "Arial 19 bold", width= 760, height = 500)
text.pack()

menu = tkin.Menu(window)


file = tkin.Menu(menu, tearoff = 0)



file.add_command(label = "New File", command = new)
file.add_command(label = "Open", command = open_file)
file.add_command(label = "Save", command = save)
file.add_command(label = "Exit", command = window.quit)

menu.add_cascade(label = "Files", menu = file)
window.config(menu= menu)

window.mainloop()