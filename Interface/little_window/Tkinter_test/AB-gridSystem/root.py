from tkinter import *
 
 

root = Tk()

text1 = Label(root, text = "Hello ladys and gentlemans")
text2 = Label(root, text = "Welcome on the show")

#o mesmo sistema de matriz so que em python o tamanho das clunas e relativo ao espaço ocupado
#pelo elementos
text1.grid(row = 0 , column = 0)
text2.grid(row = 1 , column = 0)

root.mainloop()

