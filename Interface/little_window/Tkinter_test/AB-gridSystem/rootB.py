from tkinter import *
 
 

root = Tk()

text1 = Label(root, text = "Hello ladys and gentlemans")
text2 = Label(root, text = "Welcome on the show")
text3 = Label(root, text = "Now Start")
text4 = Label(root , text = "      " ).grid(row= 3, column = 3)

#o mesmo sistema de matriz so que em python o tamanho das clunas e relativo ao espaço ocupado
#pelo elementos
text1.grid(row = 0 , column = 0)
text2.grid(row = 1, column = 9)
text3.grid(row = 2, column = 6)


root.mainloop()

