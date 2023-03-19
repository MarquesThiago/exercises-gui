from tkinter import *


root = Tk()

entry = Entry(root, width = 80, bg="blue", fg= "white", borderwidth = 5)
entry.pack()
entry.insert(1, "Digite qualquer coisa")



def clicked():
    label = Label(root, text = entry.get() )
    label.pack()

    
button = Button(root, text = "CLick Me, Please", state = DISABLED, padx = 30, pady = 20 )
button2 = Button(root, text = "Add Text", padx = 30, pady = 20, command= clicked, fg = "white", bg= "#9999ff" )
button.pack()
button2.pack()



root.mainloop()